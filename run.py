#coding=utf-8
__author__ = 'messageoom'
import json
import inspect
import argparse
import unittest
import traceback
import HTMLTestRunner
import run_config
import interfaceAuth
from tools import utils
from tests.interface import IVR,Customer_Management
#Test Case Suite  ---> You must import the use case set module

log_util = utils
modules = [IVR,Customer_Management]
cases_map = dict()
cases_doc = dict()
module_cases_map = dict()

for module in modules:
    module_cases = dict()
    for func_name, func in inspect.getmembers(
        module, predicate=lambda x: inspect.isfunction(x)
    ):
        if not func_name.startswith('_'):
            case = '.'.join([module.__name__, func_name])
            cases_map[case] = func
            module_cases[case] = func
            cases_doc[case] = func.__doc__
    module_cases_map[module.__name__] = module_cases

def run():
    test_dir = './tests'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')

    #指定生成报告的路径
    filePath = "./report/MsAutoTestResult.html"
    fp = file(filePath,'wb')
    #生成报告的Title,描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='MsStock Test Report',description='This  is MsStock Test  Report')
    runner.run(suite)

def read_conf(config=None):
    config = './.conf.json' if config is None else config
    try:
        with open(config, 'r') as f:
            conf = json.loads(f.read())
            return conf
    except IOError as e:
        raise IOError(e)

def execute_task(cases=None, config=None, debug=None,emil=None,type=None ):
    """
    :param cases:
    :param config:
    :param debug:
    :param emil:
    :param type:
    :return:
    """
    if cases is None:
        cases = cases_map.keys()
    else:
        module_cases = cases.split(',')
        cases = list()
        for case in module_cases:
            if case in module_cases_map.keys():
                cases += module_cases_map[case].keys()
            elif case in cases_map.keys():
                cases.append(case)
            else:
                raise Exception('%s is not an existed module.' % case)
    conf_file = read_conf(config)
    case_names = conf_file.keys()
    # Auth
    interfaceAuth.loginSys()
    log_util.log_start()
    for case in cases:
        if case_names is not None:
            confs = conf_file[case] if case in case_names else None
            if confs is not None:
                for conf in confs:
                    try:
                        cases_map[case](conf=conf)
                        log_util.log_execute(case, 'SUCCESSFUL')
                    except Exception as e:
                        log_util.log_execute(case, 'FAILED')
                        msg = traceback.format_exc()
                        if debug is not None:
                            print msg

            else:
                try:
                    cases_map[case]()
                    log_util.log_execute(case, 'SUCCESSFUL')
                except Exception as e:
                    log_util.log_execute(case, 'FAILED')
                    msg = traceback.format_exc()
                    if debug is not None:
                        print msg

    log_util.log_result()
    log_util.log_end()
    log_util.deleteCookies()
    # TODO 剩余各参数的执行

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d', '--debug',
        action='store_true',
        dest='DEBUG',
        default=None,
        help='Print debug message.'
    )
    parser.add_argument(
        '-s', '--server',
        dest='SERVER',
        default='crm.guxiansheng.cn',
        help='Server of guxianshengCRM.'
    )
    parser.add_argument(
        '-p', '--port',
        dest='PORT',
        default='80',
        help='Port of guxianshengCRM.'
    )
    parser.add_argument(
        '-c', '--cases',
        dest='CASES',
        default=None,
        help='Testcases to run, split with ",".'
    )
    parser.add_argument(
        '-f', '--config-file',
        dest='CONF',
        default=None,
        help='Extra config of testcases, otherwise use default conf.json'
    )
    parser.add_argument(
        '-l', '--list',
        action='store_true',
        dest='LIST',
        default=None,
        help='List all testcases.'
    )
    parser.add_argument(
        '-i', '--info',
        dest='CASE',
        default=None,
        help='Get info of given testcase.'
    )

    parser.add_argument(
        '-e','--email',
        dest='EMAIL',
        default='messageoom@163.com',
        help='Send report to mail'
    )
    parser.add_argument(
        '-t','--type',
        dest='TYPE',
        default=None,
        help='Specify the type of test,Type is requests and selenium'
    )
    args = parser.parse_args()

    #print args

    run_config.SERVER = args.SERVER
    run_config.PORT = args.PORT
    run_config.DEBUG = args.DEBUG
    run_config.EMAIL = args.EMAIL
    run_config.TYPE = args.TYPE

    if args.LIST:
        for case in sorted(cases_map.keys()):
            print case
            log_util.deleteCookies()
    elif args.CASE:
        if args.CASE in cases_map.keys():
            print '\n'
            print args.CASE
            print cases_doc[args.CASE]
            log_util.deleteCookies()
    else:
        execute_task(args.CASES, args.CONF, args.DEBUG,args.EMAIL, args.TYPE)
        log_util.deleteCookies()
        # TODO
    #run()
#coding=utf-8
__author__ = 'messageoom'
import inspect
import argparse
import unittest
import HTMLTestRunner
import config

from tests.interface import test

modules = [test]
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
    args = parser.parse_args()

    config.SERVER = args.SERVER
    config.PORT = args.PORT
    config.DEBUG = args.DEBUG

    if args.LIST:
        for case in sorted(cases_map.keys()):
            print case
    elif args.CASE:
        if args.CASE in cases_map.keys():
            print '\n'
            print args.CASE
            print cases_doc[args.CASE]
    else:
        print ""
        # TODO
        #exec_task(args.CASES, args.CONF, args.DEBUG)
    #run()
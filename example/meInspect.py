__author__ = 'messageoom'
import inspect
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
        print func_name
        if not func_name.startswith('_'):
            case = '.'.join([module.__name__, func_name])
            print case
            cases_map[case] = func
            module_cases[case] = func
            cases_doc[case] = func.__doc__
    module_cases_map[module.__name__] = module_cases
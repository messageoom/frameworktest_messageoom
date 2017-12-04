__author__ = 'messageoom'
import json
def read_conf(config=None):
    config = '../.conf.json' if config is None else config
    try:
        with open(config, 'r') as f:
            conf = json.loads(f.read())
            return conf
    except IOError as e:
        raise IOError(e)

conf_file = read_conf()
print conf_file["tests.interface.test.getcalllist_001"][0]
case_names = conf_file.keys()
#print case_names
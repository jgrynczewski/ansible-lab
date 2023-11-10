import sys
import yaml
import pprint

yaml_file = sys.argv[1]
data = yaml.load(open(yaml_file).read(), Loader=yaml.FullLoader)
pprint.pprint(data)

import yaml

def parse_yaml(path):
    with open(path) as file:
        return yaml.load(file, Loader=yaml.FullLoader)
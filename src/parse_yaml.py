import os
import ast
import yaml
from .global_variable import GlobVar


def parse_yaml(path):
    root_config_dir = os.path.dirname(path)
    data = None
    with open(path) as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    str_data = str(data)
    semi_abspath = root_config_dir.replace(GlobVar.ProjectRootDir, '.')
    if "${PWD}" in str_data:
        print("warning: Since there is a path argument, you may have to perform invocation in the root directory")
    str_data = str_data.replace('${PWD}', semi_abspath)
    assert not "${PWD}" in str_data
    data = ast.literal_eval(str_data)
    assert type(data) is dict
    return data
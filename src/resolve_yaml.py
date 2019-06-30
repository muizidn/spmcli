import os, glob
from sys import exit
import yaml
from .find_config import __CONFIGFILE_NAME__, __PACKAGE_SWIFT__, find_config
from .parse_yaml import parse_yaml

__SPMCLI_LOCK__ = 'SPMCLI.lock'

def resolve_yaml():
    root_config_path = find_config()
    root_dir = os.path.dirname(root_config_path)
    checkout_path = root_dir + '/.build/checkouts'
    if not os.path.isdir(checkout_path):
        config = parse_yaml(root_config_path)
        return calculate_resolved_config([config], root_dir)
    dep_dirs = [f"{checkout_path}/{e}" for e in os.listdir(checkout_path)]
    dep_config_paths = []
    for _dir in dep_dirs:
        if glob.glob(_dir + "/SPMCLI.yaml"):
            os.chdir(_dir)
            config_path = os.path.abspath(__CONFIGFILE_NAME__)
            dep_config_paths.append(config_path)

    os.chdir(root_dir)

    config_paths = [root_config_path] + dep_config_paths
    configs = [parse_yaml(e) for e in config_paths]
    return calculate_resolved_config(configs, root_dir)

# Need to be optimized
def calculate_resolved_config(configs, path):
    resolved_config = {}
    if not configs: 
        return resolved_config
    if len(configs) == 1:
        resolved_config = configs[0]
    else:
        for config in configs:
            resolved_config = merge(resolved_config, config)
    
    with open(f"{path}/{__SPMCLI_LOCK__}", "w") as f:
        yaml.dump(resolved_config, f)
    return resolved_config

# Optimize if needed
def merge(obj1, obj2):
    obj1_t = type(obj1)
    obj2_t = type(obj2)

    if obj1 == obj2:
        return obj1
        
    if obj1_t is dict and obj2_t is dict:
        table = {}
        for key in obj1.keys():
            if obj2.get(key):
                table[key] = merge(obj1[key], obj2[key])
            else:
                table[key] = None
        for key in obj2.keys():
            if not obj1.get(key):
                table[key] = obj2[key]
        return table
    else:
        if not obj1_t is list and not obj2_t is list:
            return remove_duplicate([obj1, obj2])
        elif obj1_t is list and not obj2_t is list:
            return remove_duplicate(obj1 + [obj2])
        elif not obj1_t is list and obj2_t is list:
            return remove_duplicate([obj1] + obj2)
        elif obj1_t is list and obj2_t is list:
            return remove_duplicate(obj1 + obj2)
        else:
            print(f"Type unrecognized: obj1 > {type(obj1)}, obj2 > {type(obj2)}")
            print("Please check SPMCLI.yaml files")
            exit(1)

def remove_duplicate(obj):
    return list(set(obj))
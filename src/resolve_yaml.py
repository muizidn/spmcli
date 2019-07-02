import os, glob
from sys import exit
import yaml
from .find_config import __CONFIGFILE_NAME__, __PACKAGE_SWIFT__, find_config
from .parse_yaml import parse_yaml

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
# This still returns raw config which is not
# visually readable by user
# e,g option argument is sometimes encoded as dict rather that list
def calculate_resolved_config(configs, path):
    resolved_config = {}
    if not configs: 
        return resolved_config
    if len(configs) == 1:
        resolved_config = configs[0]
    else:
        for config in configs:
            resolved_config = merge(resolved_config, config)
    
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
            elif obj1[key]:
                table[key] = obj1[key]
            else:
                table[key] = None
        for key in obj2.keys():
            if not obj1.get(key):
                table[key] = obj2[key]
        return table
    else:
        # This is the 'algorithm' that made SPMCLI feature possible
        assert not (obj1_t is dict and obj2_t is dict)
        # String and List value is converted to dict
        if not obj1_t is dict:
            if obj1_t is list:
                obj1 = dict.fromkeys(obj1, None)
            else:
                obj1 = { obj1: None }
        if not obj2_t is dict:
            if obj2_t is list:
                obj2 = dict.fromkeys(obj2, None)
            else:
                obj2 = { obj2: None }
        # Dict to list
        # If dict key has value then put it sequentially
        # else put the key as argument
        option_args = []
        obj = { **obj1, **obj2 }
        for (key, value) in obj.items():
            if value:
                option_args.append(key)
                option_args.append(value)
            else:
                option_args.append(key)
        return option_args
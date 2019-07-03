import os
import re
from sys import exit
from .check_platform import check_platform
from .find_config import find_config
from .parse_yaml import parse_yaml
from .global_variable import __MAC__, __iOS__, __GEN_XPROJ__, GlobVar, __BUILD__
from .invoke_spm import invoke_spm

__XCCONFIG__ = "xcconfig"

def generate_xproj(args, resolved_config):
    subcommand = args.subcommand
    platform = args.platform if args.platform else check_platform()
    # if not (subcommand == __GEN_XPROJ__ and (platform in [__iOS__, __MAC__])):
    #     print("Warning: You aren't in mac")
    #     pass
    # platform_config = resolved_config.get(platform)
    # if not platform_config:
    #     print(f"Platform {platform} not defined in resolved config")
    #     exit(1)
    if not subcommand == __GEN_XPROJ__:
        return
    if not platform in [__iOS__, __MAC__]:
        print('Platform not correct')
        exit(1)
    root_config_path = find_config()
    root_config = parse_yaml(root_config_path)
    xcconfig = root_config.get(__XCCONFIG__)
    if not xcconfig:
        print('Xcconfig not defined in root config')
        exit(1)
    xcconfig_file = xcconfig.get('name')
    if not xcconfig_file:
        print('Xcconfig file name not defined')
        exit(1)
    xcconfig_path = f"{GlobVar.ProjectRootDir}/{xcconfig_file}"
    list_config = read_xcconfig(xcconfig_path)
    computed_config = create_xcconfig_list(xcconfig, resolved_config[platform])
    merged_config = merge_xcconfig(list_config, computed_config)
    write_xcconfig(xcconfig_path, merged_config)
    invoke_spm(f"package generate-xcodeproj --xcconfig-overrides {xcconfig_path} --output SPMGenerated.xcodeproj")

def create_xcconfig_list(xcconfig,config):
    _config = {}
    build_config = config.get(__BUILD__)
    if not build_config:
        print("Reading configuration from build config but not found")
        exit(1)
    mapped_keys = xcconfig.get("keys")
    if not mapped_keys:
        print("Configuring xcconfig by matching between xcconfig.keys with build options but keys not found")
        exit(1)
    for (key, value) in mapped_keys.items():
        item = build_config.get(value)
        if not item:
            print(f"Xcconfig require {key} which is {value} values but {value} not found in build config")
            item  = [""]
        config_value = ""
        for i in item:
            config_value += f"{i} "
        _config[key] = config_value
    return _config

def merge_xcconfig(read_xcconfig, computed_xcconfig):
    _merged = read_xcconfig
    for c in computed_xcconfig.keys():
        _merged[c] = computed_xcconfig[c]
    return _merged

def read_xcconfig(path):
    _config = {}
    if not os.path.isfile(path):
        return _config
    with open(path, 'r') as file:
        for line in file.readlines():
            match = re.match(r"(.*)[ \t]=[ \t](.*)", line)
            if not match:
                _config[line] = ''
            else:
                key = match.group(1)
                value = match.group(2)
                _config[key] = value
    return _config                

def write_xcconfig(path, config):
    with open(path, 'w') as file:
        for (key, value) in config.items():
            if not value:
                value = ''
            _config = f"{key}\t=\t$(inherited) {value}\n"
            file.write(_config)
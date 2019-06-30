from sys import argv, exit
from .check_platform import check_platform

def compute_arguments(arg, config):
    subcommand = arg.subcommand
    platfrom = arg.platfrom if arg.platfrom else check_platform()
    other = arg.other

    if not platfrom in config.keys():
        print(f"platform '{platfrom}' not defined in SPMCLI.yaml") 
        exit(1)

    return __flatmap_config(config[platfrom], subcommand) + other

def __flatmap_config(config, subcommand):
    if not subcommand in config.keys():
        print(f"subcommand '{subcommand}' not defined in SPMCLI.yaml") 
        exit(1)

    final_arg = f"{subcommand} "
    config = config[subcommand]
    for option in config.keys():
        values = config[option]
        if not values:
            final_arg += f"{option} "
            continue
            
        for value in values:
            if value is iter(value) and not value is str:
                for arg in value:
                    final_arg += f"{option} {arg} "
            else:
                final_arg += f"{option} {value} "

    return final_arg

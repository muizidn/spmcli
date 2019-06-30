from sys import argv
from .check_platform import check_platform

def compute_arguments(arg, config):
    subcommand = arg.subcommand
    platfrom = arg.platfrom if arg.platfrom else check_platform()
    other = arg.other

    # print(subcommand)
    # print(platfrom)
    # print(other)
    # print(config[platfrom])
    # print(config[platfrom][subcommand])
    return __flatmap_config(config[platfrom], subcommand) + other

def __flatmap_config(config, subcommand):
    final_arg = f"{subcommand} "
    config = config[subcommand]
    for option in config.keys():
        values = config[option]
        if not values: continue
        for value in values:
            if value is iter(value) and not value is str:
                for arg in value:
                    final_arg += f"{option} {arg} "
            else:
                final_arg += f"{option} {value} "

    return final_arg

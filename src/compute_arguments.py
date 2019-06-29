from sys import argv
from .check_platform import check_platform
from .spm.build import build

def compute_arguments(config):
    if len(argv) < 2:
        print('Error: example command -- spmcli build')
        exit(1)

    subcommand = argv[1]
    platfrom = check_platform()
    config = config[platfrom]
    if subcommand == "build":
        return build(config["build"])
    else:
        exit(1)
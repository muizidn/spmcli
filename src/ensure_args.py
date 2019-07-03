from sys import argv, exit
from re import search
from collections import namedtuple
from .check_platform import check_platform
from .global_variable import *

__COMMAND_REGEX__ = r""
cmds = '|'.join(supported_commands)
pltfms = '|'.join(supported_platforms)

def __prepare():
    global __COMMAND_REGEX__
    __COMMAND_REGEX__ =  r"(?:.*spmcli|spmcli) (" + cmds + ") *("+ pltfms + "|) *(.*)"

def ensure_args():
    __prepare()
    args_len = len(argv)
    platform = check_platform()
    error_msg = f"""
Usage: spmcli ({cmds}) ({pltfms})opt [other]opt
        
  (platform)opt         optional argument - current default = {platform}
  (other)opt            additional argument passed to swift invocation
"""
    if args_len <= 1:
        print(error_msg)
        exit(1)
    else:
        command_str = ' '.join(str(e) for e in argv)
        match = search(__COMMAND_REGEX__, command_str)
        if not match:
            print(error_msg)
            exit(1)
        else:
            ARG = namedtuple('ARG', 'subcommand platform other')
            return ARG(
                match.group(1),
                match.group(2),
                match.group(3)
            )

        

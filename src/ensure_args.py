from sys import argv
from re import search
from collections import namedtuple
from .check_platform import check_platform
from .global_variable import *

__COMMAND_REGEX__ = r"(?:\./spmcli|spmcli) (run|build|test) *(linux|mac|windows|ios|android|) *(.*)"

def ensure_args():
    args_len = len(argv)
    platform = check_platform()
    error_msg = f"""
        {argv}
        Usage: spmcli (run|build|test) (linux|mac|windows|ios|android)opt [other]opt

            (platform)opt         optional argument - current default {platform}
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
            ARG = namedtuple('ARG', 'subcommand platfrom other')
            return ARG(
                match.group(1),
                match.group(2),
                match.group(3)
            )

        

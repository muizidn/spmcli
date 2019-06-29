
__FINAL_ARG__ = ""
def add_arg(args):
    global __FINAL_ARG__
    for arg in args:
        __FINAL_ARG__ += f"{arg} "

def build(config):
    global __FINAL_ARG__
    add_arg([
        "build",
        compute_flag_arguments("Xswiftc", config),
        compute_flag_arguments("Xcc", config),
        compute_flag_arguments("Xcxx", config),
        compute_flag_arguments("Xlinker", config)
    ])
    return __FINAL_ARG__

def compute_flag_arguments(flag, config):
    if config.get(flag):
        args = ""
        for value in config.get(flag):
            args += f"-{flag} {value}"
        return args
    else:
        return ""
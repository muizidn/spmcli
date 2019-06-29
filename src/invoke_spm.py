import os, sys, traceback

def invoke_spm(args):
    full_command = f"swift {args}"
    print(f"Invoked SPM Full Command : {full_command}")
    for output in os.popen(full_command):
        print(output)
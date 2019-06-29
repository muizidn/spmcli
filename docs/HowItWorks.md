# How SPMCLI work?

First, it will search in the current directory for Configuration file called `SPMCLI.yaml`, if not found, then search it in the parent directory. This is match with how SPM works.

Once it found, then SPMCLI will parse the YAML file, compute all arguments needed for command line, then start new child process of SPM.

Very neat.
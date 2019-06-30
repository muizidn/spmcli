# How SPMCLI work?

First, it will search in the current directory for Configuration file called `SPMCLI.yaml`, if not found, then search it in the parent directory. This is match with how SPM works.

Once it found, then SPMCLI will parse the YAML file, compute all arguments needed for command line, then start new child process of SPM.

Very neat.

# Resolve dependency SPMCLI.yaml

SPMCLI will compute all SPMCLI.yaml files in root directory and dependency root directory. It will merge them and store the resolved Configuration in SMPCLI.resolved in root folder.
# How SPMCLI work?

First, it will search in the current directory for Configuration file called `SPMCLI.yaml`, if not found, then search it in the parent directory. This is match with how SPM works.

Once it found, then SPMCLI will parse the YAML file, compute all arguments needed for command line, then start new child process of SPM.

Very neat.

# Resolve dependency SPMCLI.yaml

SPMCLI will compute all SPMCLI.yaml files in root directory and dependency root directory. It will merge them and store the resolved Configuration in SMPCLI.resolved in root folder.

# Features and limitations
### Features
    1. SPMCLI allows user to write single option to be written in String rather than array
    2. It also allows option values to be written in Dictionary to maximize YAML variable & merge keys feature
    3. It will resolve ${PWD} to it's YAML directory
### Limitations
    1. a SPMCLI.yaml must be written in valid YAML document.
    2. If there any duplication in array, the latter will override.
    3. It must be ${PWD}
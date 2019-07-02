# Swift Package Manager CLI

You have bad days when should working with Swift Package Manager in command line?
1. Tedious flags
2. Or, you don't want to manage script files?

Now, it will be fun!

# Requirement
Python 3

1. Write your flags in SPMCLI.yaml
```
# SPMCLI.yaml
linux:
    build:
        -Xswiftc: 
            - "-target"
            - "-DDEBUG"
        -Xcc:
            - "-DHAVE_INTTYPES_H"
mac:
    build:
        -Xlinker:
            - "./libHello.a"
```
See example in [SPMCLI.yaml](SPMCLI.yaml)

2. Invoke `spmcli build`

# How to install
This helper script will be available through `pip`, make sure you have Python3 in your system.

For now, you can install using this way.
### Git
```
git clone git clone https://github.com/muizidn/spmcli.git
cd spmcli
pip3 install -r requirements.txt
pyinstaller --onefile spmcli
export PATH=${PWD}/dist:$PATH
#or update your .bashrc
```
###

See [HowItWorks](docs/HowItWorks.md)

# Contributing
SPMCLI is just a helper. Try to design your idea so it can be implemented in SwiftPM first, then apply it in SPMCLI. We hope SPM will provide nice way to set our configurations in the future.
But you can always make an issue. Why not?
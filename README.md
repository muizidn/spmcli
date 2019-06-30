# Swift Package Manager CLI

You have bad days when should working with Swift Package Manager in command line?
1. Tedious flags
2. Or, you don't want to manage script files?

Now, it will be fun!

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

For now, you can install using `git` and update your PATH to root directory or using PyInstaller and update PATH to dist directory.
# Swift Package Manager CLI

You have bad days when should working with Swift Package Manager in command line?
1. Tedious flags
2. Or, you don't want to manage script files?

Here let's do our work.
```
# SPMCLI.yaml

build:
    linux:
        Xswiftc: 
            - "-target"
            - "-DDEBUG"
        Xcc:
            - "-DHAVE_INTTYPES_H"
    darwin:
        Xlinker:
            - "./libHello.a"
```
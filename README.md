# Swift Package Manager CLI

You have bad days when should working with Swift Package Manager in command line?
1. Tedious flags
2. Or, you don't want to manage script files?

Here let's do our work.
```
# SPMCLI.yaml
linux:
    build:
        Xswiftc: 
            - "-target"
            - "-DDEBUG"
        Xcc:
            - "-DHAVE_INTTYPES_H"
mac:
    build:
        Xlinker:
            - "./libHello.a"
```
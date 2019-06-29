import os, glob

__CONFIGFILE_NAME__ = 'SPMCLI.yaml'
__PACKAGE_SWIFT__ = 'Package.swift'

def find_config():
    while not glob.glob(__CONFIGFILE_NAME__):
        if glob.glob(__PACKAGE_SWIFT__):
            print("Found Package.swift but no SPMCLI.yaml")
            exit(1)
        os.chdir('..')
        return find_config()
    else:
        return os.path.abspath(__CONFIGFILE_NAME__)
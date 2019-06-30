from sys import platform, exit

def check_platform():
    if platform == "linux" or platform == "linux2":
        return "linux"
    elif platform == "darwin":
        return "mac"
    elif platform == "win32":
        return "windows"
    else:
        print(f"Error: platform is {platform}")
        exit(1)
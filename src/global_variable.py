__BUILD__ = "build"
__RUN__ = "run"
__TEST__ = "test"
__GEN_XPROJ__ = "xcproj"

supported_commands = [
    __BUILD__,
    __RUN__,
    __TEST__,
    __GEN_XPROJ__
]

__LINUX__ = "linux"
__MAC__ = "mac"
__WINDOWS__ = "windows"
__ANDROID__ = "android"
__iOS__ = "ios"

supported_platforms = [
    __LINUX__,
    __MAC__,
    __WINDOWS__,
    __ANDROID__,
    __iOS__
]

class GlobVar:
    ProjectRootDir = ""
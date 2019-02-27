from conans import ConanFile, CMake, tools
from conans.tools import os_info, SystemPackageTool

import os

channel = os.getenv("CONAN_CHANNEL", "testing")
username = os.getenv("CONAN_USERNAME", "conan")

class ArduinoConan(ConanFile):
    name = "arduino-stl"
    version = "1.0.0"
    license = "LGPL"
    url = "https://github.com/Dr-QP/conan-arduino-stl"
    description = "Standard C++ for Arduino (port of uClibc++)"
    settings = "os", "compiler", "arch"
    exports_sources = "*", "!build/*", "!test_package/*", "!.travis*", "!.vs*", "!**/.DS_Store"
    source_git = "https://github.com/mike-matera/ArduinoSTL.git"

    def build_requirements(self):
        if self.settings.os == "Arduino":
            self.build_requires(self.composeRequire("arduino-toolchain/[>1.8]"))

    def composeRequire(self, packageName):
        return "%s@%s/%s" % (packageName, self.user, self.channel)
        
    # def build(self):
    #     cmake = CMake(self)
    #     cmake.configure()
    #     cmake.build()

    def package(self):
        self.copy("*")

    def package_id(self):
        self.info.header_only()
        
    def package_info(self):
        self.hea
        self.cpp_info.includedirs = ['include']
        self.cpp_info.cppflags = ['-std=c++11']
        self.cpp_info.libs = ["BOLIDE_Player"]

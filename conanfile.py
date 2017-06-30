from conans import ConanFile, CMake, tools
import os


class SpineConan(ConanFile):
    name = "spine"
    version = "3.6.32"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "src/*"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir="src".format(self.version))
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="src".format(self.version))
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["spine-c"]

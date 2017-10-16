from conans import ConanFile, CMake, tools
import os
import shutil

class SpineConan(ConanFile):
    name = "spine"
    version = "3.6.36_0"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "src/*"
    requires = "multibuilder/1.0@hi3c/experimental"


    def real_build(self, arch, triple):
        print(os.getcwd())
        shutil.copy("../conanbuildinfo.cmake", "conanbuildinfo.cmake")
        cmake = CMake(self)
        cmake.configure(source_dir=os.path.join(self.conanfile_directory, "src"),
            build_dir=os.path.join(self.conanfile_directory, "build-" + arch))
        cmake.build()

    def build(self):
        if self.settings.arch == "universal":
            with tools.pythonpath(self):
                import multibuilder
                self.build = multibuilder.MultiBuilder(self, ("armv7", "arm64", "x86_64", "i386"))
                self.build.multi_build(self.real_build)

    def package(self):
        self.copy("*.h", dst="include", src="src".format(self.version))
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", src="build-universal", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["spine-c"]

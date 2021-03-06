from conans.model.conan_file import ConanFile
from conans import CMake
import os

############### CONFIGURE THESE VALUES ##################
default_user = "lasote"
default_channel = "testing"
#########################################################

channel = os.getenv("CONAN_CHANNEL", default_channel)
username = os.getenv("CONAN_USERNAME", default_user)


class DefaultNameConan(ConanFile):
    name = "DefaultName"
    version = "0.1"
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"
    requires = "m4/1.4.14-1@%s/%s" % (username, channel)

    def build(self):
        pass
        # cmake = CMake(self)
        # cmake.configure(source_dir="../../", build_dir="./")
        # cmake.build()

    def imports(self):
        pass
        # self.copy(pattern="*.dll", dst="bin", src="bin")
        # self.copy(pattern="*.dylib", dst="bin", src="lib")

    def test(self):
        pass
        # self.run("cd bin && .%senough" % os.sep)
        # assert os.path.exists(os.path.join(self.deps_cpp_info["m4"].rootpath, "LICENSE"))

from conans import tools
import os
from conanfile_base import BaseLib

class xeyesConan(BaseLib):
    basename = "xeyes"
    name = basename.lower()
    version = "1.1.2"
    tags = ("conan", "xeyes")
    description = '{description}'
    exports = ["conanfile_base.py"]
    requires = [ 'libx11/1.6.8@bincrafters/stable',
                 'libxt/1.2.0@bincrafters/stable',
                 'libxext/1.3.4@bincrafters/stable',
                 'libxmu/1.1.3@bincrafters/stable',
                 'xproto/7.0.31@bincrafters/stable',
                 'libxrender/0.9.10@bincrafters/stable']

    def source(self):
        url = "https://www.x.org/archive/individual/app/xeyes-1.1.2.tar.gz"
        tools.get(url, sha256="4a675b34854da362bd8dff4f21ff92e0c19798b128ea0af24b7fc7c5ac2feea3")
        extracted_dir = "xeyes-" + self.version
        os.rename(extracted_dir, self._source_subfolder)
    
    def build(self):
        super(xeyesConan, self).build()
        self.run(os.path.join('source_subfolder', 'xeyes'))

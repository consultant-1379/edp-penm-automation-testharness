#undo_setup_test_harness
import os
from shutil import rmtree
from constants import *

from setup_test_harness_penm import setup_test_harness

class undo_setup_test_harness(setup_test_harness):
    def __init__(self):
        super(undo_setup_test_harness, self).__init__()
        self.dir_references = backup_files_map

    def main(self):
        if os.path.isdir(bkp_dir):
            for dir_ in os.listdir(bkp_dir):
                if dir_ in self.dir_references:
                    print("Restoring file {0} ...".format(dir_))
                    source = os.path.join(base_dir, bkp_dir, dir_)
                    dest = os.path.join(self.dir_references[dir_])
                    self.common_func_obj.copy_files(source, dest)
        for directory in [bkp_dir, base_dir + testharness_data_file_dir]:
            if os.path.isdir(directory):
                rmtree(directory)

if __name__ == '__main__':
    undo_setup_obj = undo_setup_test_harness()
    undo_setup_obj.main()


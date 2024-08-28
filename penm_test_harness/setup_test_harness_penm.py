import os
import sys
import argparse

from common import CommonFunctions
from stages.penm_init_dvms import INIT_DVMS
from stages.penm_sw_preparation import SOFTWARE_VERIFICATION
from stages.penm_pre_upgrade import PRE_UPGRADE
from stages.penm_upgrade import UPGRADE
from stages.penm_pre_upgrade_customization import PRE_UPGRADE_CUST
from stages.penm_validate_upgrade import VALIDATE_UG
from stages.penm_post_upgrade import POST_UG
from stages.penm_post_upgrade_customization import POST_UPGRADE_CUST
from stages.penm_finalize import FINALIZE_UG
from constants import *

class setup_test_harness(object):
    def __init__(self):
        self.common_func_obj = CommonFunctions()

    def setup(self, profiles, profiles_data, remove_profiles):
        self.common_func_obj.create_dirs([bkp_dir_name, testharness_data_file_dir, "ENM", "LITP", "RHEL"])
        for files in os.listdir(command_output_files_path):
            if os.path.isfile(command_output_files_path + files):
                self.common_func_obj.copy_files(command_output_files_path + files, base_dir + testharness_data_file_dir)
        self.enminst_rpm_install()
        for profile in profiles:
            profile = profile.strip()
            print(profile)
            if profile == "penm_finalize":
                pass
            if profile not in profiles_data.keys():
                print("Invalid profile {0}".format(profile))
                continue

            dyn_class = globals()[profile_classes_map[profile]]
            dyn_class(profiles_data[profile], remove_profiles)
            self.common_func_obj.print_line()
        
    def enminst_rpm_install(self):
        for artifact in os.listdir("/software/ENM/"):
            if artifact.startswith("ERICenm_CXP9027091"):
                enm_iso = artifact
                os.system("sh {0} {1}".format("data_files/enminst_install_rpm.sh", artifact))


def parse_options():
    """
    Parse options
    """
    parse = argparse.ArgumentParser()

    parse.add_argument('-all',  help='Setup Testharness',
                       action="store_true")
    parse.add_argument('-p', '--profiles',nargs='+', default=[],
            help='Setup of specified profiles',
            dest='selective_profiles')
    parse.add_argument('-r', '--remove profiles',nargs='+', default=[],
            help='Donot execute specified profiles',
            dest='remove_profiles')

    return parse.parse_args()

def main(args):
    setup_test_harness_obj = setup_test_harness()
    common_func_obj = CommonFunctions()
    profiles_data = common_func_obj.read_file("profiles.json")
    if args.all:
        del profiles_data['penm_finalize']
        profiles = profiles_data.keys()
        print(profiles)
    elif args.selective_profiles:
        profiles = args.selective_profiles
    else:
       print('Enter -all or -p <profiles>')
       sys.exit(1)
    setup_test_harness_obj.setup(profiles, profiles_data, args.remove_profiles)


if __name__ == "__main__":
    ARGS = parse_options()
    main(ARGS)

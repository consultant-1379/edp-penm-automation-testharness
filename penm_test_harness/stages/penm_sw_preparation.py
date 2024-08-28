import os
from common import CommonFunctions
from constants import *

class SOFTWARE_VERIFICATION():
    def __init__(self, stage_profiles, skip_profile):
        self.common_obj = CommonFunctions()
        for each_profile in stage_profiles:
            if not each_profile in 'mock_{0}'.format(skip_profile):
                getattr(self, each_profile)()

    def mock_penm_get_upgrade_type(self):
        print("Mocking penm_get_upgrade_type profile.....")
        self.common_obj.backup_file(penm_get_upgrade_type_file)
        self.common_obj.copy_files(data_files_dir + 'rh7_upgrade_enm.sh', penm_get_upgrade_type_file)

    def mock_penm_software_verification(self):
        self.common_obj.create_release_note_files_and_update_checksum()

    def mock_penm_disk_allocation(self):
        print("Mocking penm_disk_allocation profile...")
        self.common_obj.backup_file(enm_version_file)
        self.common_obj.copy_files(data_files_dir + 'enm_version.txt', enm_version_file)
        self.common_obj.backup_file(naviseccli_file)
        self.common_obj.copy_files(data_files_dir + 'navisecli_file_contents.sh', naviseccli_file)

    def mock_penm_update_rpms(self):
        print("Mocking penm_update_rpms profile...")
        iso_present = False
        for iso in os.listdir('/software/ENM/'):
            if iso.startswith('ERICenm_CXP9027091'):
                iso_present = True
        if not iso_present:
            print("No ENM ISO found in /software/ENM directory\nExiting...")
            quit()
        if os.system("rpm -q --queryformat '%{VERSION}' ERICenminst_CXP9030877"):
            print("ERICenminst_CXP9030877 is not installed on ENM\tExiting...")
            quit()
        self.common_obj.backup_file(pre_upgrade_script_file)
        self.common_obj.copy_files(data_files_dir + 'pre_upgrade_script_file.sh', pre_upgrade_script_file)
        self.common_obj.create_dir_path(litp_cfg_version_file)
        self.common_obj.backup_file(litp_cfg_version_file)
        self.common_obj.copy_files(data_files_dir + 'litp_cfg_version.txt', litp_cfg_version_file)
        self.common_obj.backup_file(mco_script)
        self.common_obj.copy_files(data_files_dir + 'mco_commands_file.sh', mco_script)
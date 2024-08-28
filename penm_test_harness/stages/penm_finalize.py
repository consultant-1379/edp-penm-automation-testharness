import os.path
from common import CommonFunctions
from constants import *

class FINALIZE_UG():
    def __init__(self, stage_profiles, skip_profile):
        self.common_obj = CommonFunctions()
        for each_profile in stage_profiles:
            if not each_profile in 'mock_{0}'.format(skip_profile):
                getattr(self, each_profile)()

    def mock_penm_remove_snapshots(self):
        print("Mocking penm_remove_snapshots profile...")
        self.common_obj.create_dir_path(enm_snapshots_file)
        self.common_obj.backup_file(enm_snapshots_file)
        self.common_obj.copy_files(data_files_dir + 'enm_snapshots_file.sh', enm_snapshots_file)
        self.common_obj.create_dir_path(brs_file)
        self.common_obj.backup_file(brs_file)
        self.common_obj.copy_files(data_files_dir + 'brs_file.sh', brs_file)

    def mock_penm_post_upgrade_ombs_tasks(self):
        print("Mocking penm_post_upgrade_ombs_tasks profile...")
        self.common_obj.create_dir_path(bos_file)
        self.common_obj.backup_file(bos_file)
        self.common_obj.copy_files(data_files_dir + 'bos_true', bos_file)

    def mock_penm_sfha_uplift(self):
        #print("Nothing to mock for this profile")
        pass

    def mock_penm_persist_logs(self):
        print("Mocking penm_persist_logs profile...")
        self.common_obj.create_dir_path('var/tmp/edp')  

    def mock_penm_sshd_config(self):
        #print("Nothing to mock for this profile")
        pass 

    def mock_penm_remove_sed(self):
        #print("Nothing to mock for this profile")
        pass 
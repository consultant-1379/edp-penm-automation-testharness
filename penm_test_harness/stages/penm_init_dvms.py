import os.path
from common import CommonFunctions
from constants import *

class INIT_DVMS():
    def __init__(self, stage_profiles, skip_profile):
        self.common_obj = CommonFunctions()
        for each_profile in stage_profiles:
            if not each_profile in 'mock_{0}'.format(skip_profile):
                getattr(self, each_profile)()

    def mock_penm_init_dvms(self):
        #print("Nothing to mock for penm_init_dvms profile")
        pass

    def mock_penm_verify_ms_connection(self):
        print("Mocking penm_verify_ms_connection...")
        self.common_obj.backup_file(litp_commands_file)
        self.common_obj.copy_files(data_files_dir + 'litp_file.sh', litp_commands_file)

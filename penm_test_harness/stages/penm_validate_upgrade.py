import os.path
from common import CommonFunctions
from constants import *

class VALIDATE_UG():
    def __init__(self, stage_profiles, skip_profile):
        self.common_obj = CommonFunctions()
        for each_profile in stage_profiles:
            if not each_profile in 'mock_{0}'.format(skip_profile):
                getattr(self, each_profile)()

    def mock_penm_healthcheck(self):
        print("Mocking penm_healthcheck...")
        self.common_obj.backup_file(penm_healthcheck_file)
        self.common_obj.copy_files(data_files_dir + 'enm_healthcheck.txt', penm_healthcheck_file)
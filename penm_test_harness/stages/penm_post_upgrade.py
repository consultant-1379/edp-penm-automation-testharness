import os.path
from common import CommonFunctions
from constants import *

class POST_UG():
    def __init__(self, stage_profiles, skip_profile):
        self.common_obj = CommonFunctions()
        for each_profile in stage_profiles:
            if not each_profile in 'mock_{0}'.format(skip_profile):
                getattr(self, each_profile)()

    def mock_penm_enable_elex(self):
        print("Mocking penm_enable_elex profile...")
        self.common_obj.create_dir_path('/ericsson/enm/alex/mock')
        self.common_obj.os_execute_command("mount /dev/vda2 /ericsson/enm/alex")

    def mock_penm_post_upgrade_license_check(self):
        #print("Nothing to mock in penm_post_upgrade_license_check profile")
        pass

    def mock_penm_post_upgrade_minilink_cm(self):
        #print("Nothing to mock for penm_post_upgrade_minilink_cm profile")
        pass

    def mock_penm_enable_geor_cronjobs(self):
        #print("Nothing to mock for penm_enable_geor_cronjobs profile")
        pass

    def mock_penm_verify_ipmi_settings(self):
        #print("Nothing to mock for penm_verify_ipmi_settings profile")
        pass
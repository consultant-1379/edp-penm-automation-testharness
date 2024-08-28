import os.path
from common import CommonFunctions
from constants import *

class POST_UPGRADE_CUST():
    def __init__(self, stage_profiles, skip_profile):
        self.common_obj = CommonFunctions()
        for each_profile in stage_profiles:
            if not each_profile in 'mock_{0}'.format(skip_profile):
                getattr(self, each_profile)()

    def mock_penm_post_upgrade_customization(self):
        #print("Nothing to mock for this profile")
        pass
import os.path
from common import CommonFunctions
from constants import *

class PRE_UPGRADE_CUST():
    def __init__(self, stage_profiles, skip_profile):
        self.common_obj = CommonFunctions()
        self.mock_penm_pre_upgrade_customization()

    def mock_penm_pre_upgrade_customization(self):
        #print("Nothing to mock for this profile")
        pass
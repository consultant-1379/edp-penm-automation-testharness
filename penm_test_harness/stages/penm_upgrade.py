import os.path
from common import CommonFunctions
from constants import *

class UPGRADE():
    def __init__(self, stage_profiles, skip_profile):
        self.common_obj = CommonFunctions()
        for each_profile in stage_profiles:
            if not each_profile in 'mock_{0}'.format(skip_profile):
                getattr(self, each_profile)()

    def mock_penm_kickstart_ms(self):
        #print("This stage will be called as part of 6 to 7 upgrade")
        pass

    def mock_penm_init_ms(self):
        #print("This stage will be called as part of 6 to 7 upgrade")
        pass

    def mock_penm_install_ms(self):
        #print("This stage will be called as part of 6 to 7 upgrade")
        pass

    def mock_penm_restore_ms(self):
        #print("This stage will be called as part of 6 to 7 upgrade")
        pass

    def mock_penm_pre_uplift_checks(self):
        #print("This stage will be called as part of 6 to 7 upgrade")
        pass

    def mock_penm_upgrade_software(self):
        print("Mocking penm_upgrade_software...")
        self.common_obj.create_dir_path('/vol1/.dvms_on_ms/mock')
        self.common_obj.backup_file(litp_commands_file)
        self.common_obj.copy_files(data_files_dir + 'litp_file.sh', litp_commands_file)
        self.common_obj.backup_file(ms_log_msg_enminst_log_function)
        self.common_obj.create_dir_path(ms_log_msg_enminst_log_function)
        self.common_obj.os_execute_command('touch /opt/ericsson/enminst/lib/h_logging/__init__.py')
        self.common_obj.copy_files(data_files_dir + 'enminst_logger.py', ms_log_msg_enminst_log_function)

        self.common_obj.backup_file(redhat_release_file)
        self.common_obj.copy_files(data_files_dir + 'redhat_release_file.txt', redhat_release_file)
        self.common_obj.backup_file(rhel_patch_set_version_file)
        self.common_obj.copy_files(data_files_dir + 'rhel_patch_set-version_file.txt', rhel_patch_set_version_file)
        self.common_obj.backup_file(rhel7_patch_set_version_file)
        self.common_obj.copy_files(data_files_dir + 'rhel7_patch_set-version_file.txt', rhel7_patch_set_version_file)
        self.common_obj.backup_file(rhel79_patch_set_version_file)
        self.common_obj.copy_files(data_files_dir + 'rhel79_patch_set-version.txt', rhel79_patch_set_version_file)
        self.common_obj.backup_file(litp_release_version)
        self.common_obj.copy_files(data_files_dir + 'litp_version_file.txt', litp_release_version)
        self.common_obj.backup_file(enm_version_file)
        self.common_obj.copy_files(data_files_dir + 'enm_version.txt', enm_version_file)
        self.common_obj.backup_file(enm_upgrade_file)
        self.common_obj.copy_files(data_files_dir + 'enm_upgrade.sh', enm_upgrade_file)

    def mock_penm_osuplift_upgrade_software(self):
        #print("This stage will be called as part of 6 to 7 upgrade")
        pass













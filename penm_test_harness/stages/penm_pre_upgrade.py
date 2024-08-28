import os.path
from common import CommonFunctions
from constants import *

class PRE_UPGRADE():
    def __init__(self, stage_profiles, skip_profile):
        self.common_obj = CommonFunctions()
        for each_profile in stage_profiles:
            if not each_profile in 'mock_{0}'.format(skip_profile):
                getattr(self, each_profile)()

    def mock_penm_pre_upgrade_healthcheck(self):
        print("Mocking penm_pre_upgrade_healthcheck")
        self.common_obj.backup_file(penm_healthcheck_file)
        self.common_obj.copy_files(data_files_dir + 'enm_healthcheck.sh', penm_healthcheck_file)

    def mock_penm_pre_upgrade_checks(self):
        print("Mocking penm_pre_upgrade_checks")
        self.common_obj.create_release_note_files_and_update_checksum()
        self.common_obj.backup_file(enm_version_file)
        self.common_obj.copy_files(data_files_dir + 'enm_version.txt', enm_version_file)
        self.common_obj.create_dir_path(get_cluster_nodes_from_dd_file)
        self.common_obj.backup_file(get_cluster_nodes_from_dd_file)
        self.common_obj.copy_files(data_files_dir + 'cluster_dd_data.py', get_cluster_nodes_from_dd_file)
        self.common_obj.create_dir_path(backup_deployment_model_file)
        self.common_obj.backup_file(backup_deployment_model_file)
        self.common_obj.copy_files(data_files_dir + 'deployment_model_backup.txt', backup_deployment_model_file)
        self.common_obj.copy_files(data_files_dir + 'deployment_model_backup.txt', dd_xm_file_path)
        #self.common_obj.backup_file(backup_enminst_working_file)
        #self.common_obj.copy_files(data_files_dir + 'enminst_working_file.cfg', backup_enminst_working_file)
        self.common_obj.create_dir_path(encrypt_passwords_file)
        self.common_obj.backup_file(encrypt_passwords_file)
        self.common_obj.copy_files(data_files_dir + 'encrypt_passwords.py', encrypt_passwords_file)
        self.common_obj.create_dir_path(substituteParams_file)
        self.common_obj.backup_file(substituteParams_file)
        self.common_obj.copy_files(data_files_dir + 'substituteParams.sh', substituteParams_file)
        os.chmod(substituteParams_file, 0o755)
        self.common_obj.create_dir_path(enm_upgrade_prechecks_file)
        self.common_obj.backup_file(enm_upgrade_prechecks_file)
        self.common_obj.copy_files(data_files_dir + 'enm_upgrade_prechecks.txt', enm_upgrade_prechecks_file)
        self.common_obj.create_dir_path(mco_script)
        self.common_obj.backup_file(mco_script)
        self.common_obj.copy_files(data_files_dir + 'mco_commands_file.sh', mco_script)

    def mock_penm_pre_upgrade_nas_checks(self):
        print("Mocking penm_pre_upgrade_nas_checks")
        self.common_obj.copy_files(data_files_dir + 'litp_python_path.txt', litp_python_path)
        if not os.path.exists(litp_enc_file):
            self.common_obj.create_dir_path(litp_enc_file)
            self.common_obj.os_execute_command('touch /opt/ericsson/nms/litp/lib/litp/__init__.py')
            self.common_obj.os_execute_command('touch /opt/ericsson/nms/litp/lib/litp/encryption/__init__.py')
        self.common_obj.create_dir_path(litp_enc_file)
        self.common_obj.backup_file(litp_enc_file)
        self.common_obj.copy_files(data_files_dir + 'encryption.py', litp_enc_file)
        self.common_obj.copy_files(data_files_dir + 'litp_security.txt', litp_security_file)
        self.common_obj.backup_file(remote_command_file)
        self.common_obj.copy_files(data_files_dir + 'remote_command.py', remote_command_file)
        self.common_obj.create_dir_path(keyset1_file)
        self.common_obj.backup_file(keyset1_file)
        self.common_obj.copy_files(data_files_dir + 'keyset1_file.txt', keyset1_file)
        self.common_obj.create_dir_path(litp_shadow_file)
        self.common_obj.backup_file(litp_shadow_file)
        self.common_obj.copy_files(data_files_dir + 'litp_shadow_file.txt', litp_shadow_file)
        self.common_obj.create_dir_path(nasAudit_file)
        self.common_obj.backup_file(nasAudit_file)
        self.common_obj.copy_files(data_files_dir + 'nasAudit_file.py', nasAudit_file)
        os.chmod(nasAudit_file, 0o755)
        self.common_obj.backup_file(penm_healthcheck_file)
        self.common_obj.copy_files(data_files_dir + 'enm_healthcheck.sh', penm_healthcheck_file)
        self.common_obj.create_dir_path(nas_version_file)
        self.common_obj.backup_file(nas_version_file)
        self.common_obj.copy_files(data_files_dir + 'nas_version_file.txt', nas_version_file)
        self.common_obj.backup_file(redhat_release_file)
        self.common_obj.copy_files(data_files_dir + 'redhat_release_file.txt', redhat_release_file)
        self.common_obj.create_dir_path(ericrhel7_release_file)
        self.common_obj.backup_file(ericrhel7_release_file)
        self.common_obj.copy_files(data_files_dir + 'ericrhel7_release_file.txt', ericrhel7_release_file)
        self.common_obj.create_dir_path(ericrhel79_release_file)
        self.common_obj.backup_file(ericrhel79_release_file)
        self.common_obj.copy_files(data_files_dir + 'ericrhel79_release_file.txt', ericrhel79_release_file)

    def mock_penm_pre_upgrade_remove_snapshots(self):
        print("Mocking penm_pre_remove_snapshots profile...")
        self.common_obj.create_dir_path(enm_snapshots_file)
        self.common_obj.backup_file(enm_snapshots_file)
        self.common_obj.copy_files(data_files_dir + 'enm_snapshots_file.sh', enm_snapshots_file)
        self.common_obj.create_dir_path(brs_file)
        self.common_obj.backup_file(brs_file)
        self.common_obj.copy_files(data_files_dir + 'brs_file.sh', brs_file)

    def mock_penm_pre_upgrade_ombs_tasks(self):
        print("Mocking penm_pre_upgrade_ombs_tasks")
        self.common_obj.create_dir_path(bpclimagelist_file)
        if os.path.isfile(backup_conf_file):
            self.common_obj.backup_file(backup_conf_file)
        self.common_obj.copy_files(data_files_dir + 'bp.conf', backup_conf_file)
        if os.path.isfile(bpclimagelist_file):
            self.common_obj.backup_file(bpclimagelist_file)
        self.common_obj.os_execute_command('useradd brsadm')
        self.common_obj.copy_files(data_files_dir + 'bpclimagelist', bpclimagelist_file)
        os.chmod(bpclimagelist_file, 0o755)
        self.common_obj.create_dir_path(bos_file)
        self.common_obj.backup_file(bos_file)
        self.common_obj.copy_files(data_files_dir + 'bos_false', bos_file)
        if os.path.exists(bkp_lock_file):
            os.unlink(bkp_lock_file)
        self.common_obj.backup_file(brs_file)
        self.common_obj.copy_files(data_files_dir + 'brs_file.sh', brs_file)

    def mock_penm_pre_upgrade_ombs_checks(self):
        print("Mocked as part of penm_pre_upgrade_ombs_tasks")

    def mock_penm_upgrade_customisations(self):
        print("Mocking penm_upgrade_customisations profile...")
        self.common_obj.create_dir_path('/var/www/html/ENM_ms/mock')
        self.common_obj.copy_files(rpms_path + 'ERICenmdeploymenttemplates_CXP9031758-2.11.1.rpm', ms_rpms_path + "ERICenmdeploymenttemplates_CXP9031758-2.11.1.rpm")
        self.common_obj.create_dir_path('/ericsson/deploymentDescriptions/customization/mock')
        self.common_obj.os_execute_command("cp -r {0} {1}".format(command_output_files_path + "customization/*", customization_path))

    def mock_penm_disable_geor_cronjobs(self):
        # Data mocked using litp and other modules
        #print("Nothing to mock for this profile")
        pass

    def mock_penm_increase_import_timeout(self):
        # Data mocked using litp and other modules
        #print("Nothing to mock for this profile")
        pass

    def mock_penm_check_admin_user(self):
        print("Mocking penm_check_admin_user profile...")
        self.common_obj.backup_file(litp_commands_file)
        self.common_obj.copy_files(data_files_dir + 'litp_file.sh', litp_commands_file)
        self.common_obj.backup_file(mco_script)
        self.common_obj.copy_files(data_files_dir + 'mco_commands_file.sh', mco_script)
        self.common_obj.create_dir_path(psql_binary)
        self.common_obj.backup_file(psql_binary)
        self.common_obj.copy_files(data_files_dir + 'psql.sh', psql_binary)
        self.common_obj.create_dir_path('/ericsson/tor/data/idenmgmt/mock')
        self.common_obj.create_dir_path(postgresql01_passkey_file)
        self.common_obj.backup_file(postgresql01_passkey_file)
        self.common_obj.copy_files(data_files_dir + 'postgresql01_passkey.txt', postgresql01_passkey_file)

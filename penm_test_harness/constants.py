from distutils.sysconfig import get_python_lib

profile_classes_map = {'penm_init_dvms': 'INIT_DVMS', 'penm_sw_preparation': 'SOFTWARE_VERIFICATION',
     'penm_pre_upgrade_checks': 'PRE_UPGRADE', 'penm_pre_upgrade': 'PRE_UPGRADE',
     'penm_pre_upgrade_customization': 'PRE_UPGRADE_CUST', 'penm_upgrade': 'UPGRADE',
     'penm_validate_upgrade': 'VALIDATE_UG', 'penm_post_upgrade_customization': 'POST_UPGRADE_CUST',
     'penm_post_upgrade': 'POST_UG', 'penm_finalize': 'FINALIZE_UG'}


python_sitemap = get_python_lib()
base_dir = "/software/"
bkp_dir_name = "EDP_bkp_dir"
bkp_dir = "/software/{0}".format(bkp_dir_name)
testharness_data_file_dir = 'testharness_data_files'

data_files_dir = "data_files/"
command_output_files_path = "data_files/command_output_files/"
rpms_path = "data_files/rpms/"
litp_commands_file = '/usr/bin/litp'
litp_release_version = '/etc/litp-release'
release_note = '/software/ENM/releasenote.json'
naviseccli_file = '/opt/Navisphere/bin/naviseccli'
enm_version_file = '/etc/enm-version'
ms_log_msg_enminst_log_function = '/opt/ericsson/enminst/lib/h_logging/enminst_logger.py'
pre_upgrade_script_file = '/opt/ericsson/enminst/bin/pre_upgrade_rpms.sh'
mco_script = '/usr/bin/mco'
psql_binary = '/usr/bin/psql'
enm_snapshots_file = '/opt/ericsson/enminst/bin/enm_snapshots.bsh'
brs_file = '/opt/ericsson/itpf/bur/bin/brs'
litp_cfg_version_file = '/opt/ericsson/nms/litp/etc/puppet/litp_config_version'
redhat_release_file = '/etc/redhat-release'
rhel_patch_set_version_file = '/etc/rhel_patch_set-version'
rhel7_patch_set_version_file = '/etc/rhel7_patch_set-version'
penm_healthcheck_file = '/opt/ericsson/enminst/bin/enm_healthcheck.sh'
get_cluster_nodes_from_dd_file = '/opt/ericsson/enminst/lib/h_litp/litp_rest_client.py'
backup_deployment_model_file='/opt/ericsson/enminst/runtime/enm_deployment.xml'
backup_enminst_working_file = '/opt/ericsson/enminst/runtime/enminst_working.cfg'
enm_upgrade_prechecks_file = '/opt/ericsson/enminst/bin/enm_upgrade_prechecks.sh'
keyset1_file = '/opt/ericsson/nms/litp/keyset/keyset1'
litp_shadow_file = '/opt/ericsson/nms/litp/etc/litp_shadow'
nasAudit_file = '/opt/ericsson/NASconfig/bin/nasAudit.py'
nas_version_file = '/opt/VRTSnas/conf/prod_version.conf'
backup_conf_file = '/usr/openv/netbackup/bp.conf'
bpclimagelist_file = '/usr/openv/netbackup/bin/bpclimagelist'
bos_file = '/opt/ericsson/itpf/bur/bin/bos'
bkp_lock_file = '/opt/ericsson/itpf/bur/data/backup_metadata/bkp_lock'
ericrhel7_release_file = '/etc/ericrhel7-release'
ericrhel79_release_file = '/etc/ericrhel79-release'
encrypt_passwords_file = '/opt/ericsson/enminst/lib/encrypt_passwords.py'
substituteParams_file = '/opt/ericsson/enminst/bin/substituteParams.sh'
postgresql01_passkey_file = '/ericsson/tor/data/idenmgmt/postgresql01_passkey'
litp_python_path = python_sitemap + '/litp.pth'
litp_enc_file = '/opt/ericsson/nms/litp/lib/litp/encryption/encryption.py'
litp_security_file = '/etc/litp_security.conf'
remote_command_file = python_sitemap + '/paramiko/__init__.py'
enm_upgrade_file = '/opt/ericsson/enminst/bin/upgrade_enm.sh'
ms_rpms_path = '/var/www/html/ENM_ms_rhel7/'
customization_path = '/ericsson/deploymentDescriptions/customization'
dd_xm_file_path = '/ericsson/deploymentDescriptions/large__production_test_dd.xml'
rhel79_patch_set_version_file = '/etc/rhel79_patch_set-version'
penm_get_upgrade_type_file = '/var/tmp/enm_inst//opt/ericsson/enminst/bin/rh7_upgrade_enm.sh'

backup_files_map = {"litp": litp_commands_file,
                    "enm-version": enm_version_file,
                    "naviseccli": naviseccli_file,
                    "pre_upgrade_rpms.sh": pre_upgrade_script_file,
                    "mco": mco_script,
                    "litp_config_version": litp_cfg_version_file,
                    "enminst_logger.py": ms_log_msg_enminst_log_function,
                    "redhat-release": redhat_release_file,
                    "rhel_patch_set-version": rhel_patch_set_version_file,
                    "rhel7_patch_set-version": rhel7_patch_set_version_file,
                    "litp-release": litp_release_version,
                    "enm_snapshots.bsh": enm_snapshots_file,
                    "brs": brs_file,
                    "psql": psql_binary,
                    "enm_healthcheck.sh": penm_healthcheck_file,
                    "enm_upgrade_prechecks.sh": enm_upgrade_prechecks_file,
                    "keyset1": keyset1_file,
                    "litp_shadow": litp_shadow_file,
                    "nasAudit.py": nasAudit_file,
                    "version.conf": nas_version_file,
                    "bp.conf": backup_conf_file,
                    "bpclimagelist": bpclimagelist_file,
                    "bos": bos_file,
                    "ericrhel7-release": ericrhel7_release_file,
                    "ericrhel79-release": ericrhel79_release_file,
                    "substituteParams.sh": substituteParams_file,
                    "encrypt_passwords.py": encrypt_passwords_file,
                    "postgresql01_passkey": postgresql01_passkey_file,
                    "litp_rest_client.py":  get_cluster_nodes_from_dd_file,
                    "enm_deployment.xml": backup_deployment_model_file,
                    "enminst_working.cfg": backup_enminst_working_file,
                    "encryption.py": litp_enc_file,
                    "litp_security.conf": litp_security_file,
                    "__init__.py": remote_command_file,
                    "upgrade_enm.sh": enm_upgrade_file,
                    "rhel79_patch_set-version": rhel79_patch_set_version_file,
                    "rh7_upgrade_enm.sh": penm_get_upgrade_type_file
                    }

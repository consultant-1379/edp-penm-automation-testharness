class SSHClient():

    def set_missing_host_key_policy(self, host_key):
        pass

    def connect(self, hostname, port, pkey, username='root', password='12shroot', timeout=None, allow_agent=True, look_for_keys=False):
        pass

    def exec_command(self, command,bufsize=-1,timeout=None,get_pty=False,environment=None):
        if command == '/opt/ericsson/NASconfig/bin/nasAudit.py':
            return ('',open('/software/testharness_data_files/nasAudit.txt','r'), open('/software/testharness_data_files/no_error.txt','r'))
        if command == 'cat /opt/VRTSnas/conf/prod_version.conf':
            return ('',open('/opt/VRTSnas/conf/prod_version.conf', 'r'), open('/software/testharness_data_files/no_error.txt','r'))
        if command == 'cat /etc/redhat-release':
            return ('',open('/etc/redhat-release', 'r'), open('/software/testharness_data_files/no_error.txt','r'))
        if command == 'cat /etc/ericrhel7-release':
            return ('',open('/etc/ericrhel7-release', 'r'), open('/software/testharness_data_files/no_error.txt','r'))
        if command == 'cat /etc/ericrhel79-release':
            return ('',open('/etc/ericrhel79-release', 'r'), open('/software/testharness_data_files/no_error.txt','r'))
        if command == 'rpm -qi ERICnasconfig_CXP9033343':
            return ('',open('/software/testharness_data_files/ERICnasconfig_CXP9033343.txt', 'r'), open('/software/testharness_data_files/no_error.txt','r'))

class RSAKey():

    def from_private_key_file(self, private_key):
        pass

class AutoAddPolicy():
    pass

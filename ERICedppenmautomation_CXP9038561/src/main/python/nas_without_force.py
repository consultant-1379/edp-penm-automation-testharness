#!/usr/bin/python
import pexpect
import time
import os
import commands
os.system("touch top_output.txt")
os.system("top -b -n 1&>>top_output.txt")
print("waiting5minutes")
time.sleep(300)
print("executing script")
cmd="python /opt/ericsson/firmwareupgradetool/firmware_upgrade.py --nas --sedfile='/opt/ericsson/firmwareupgradetool/template/my_template' --username='root' --noreboot"
child=pexpect.spawn(cmd)
print("paswdprompt")
child.expect("Enter the Sudo user password                       :")
child.sendline("ZXcvb123!")
print("sentpasswd")
time.sleep(1800)
os.chdir("/var/log/FirmwareUpgrade/")
cmd="ls -lrt enm_fw_upg_* | tail -1 |awk -F\" \" '{print $9}'"
output=commands.getoutput(cmd)
print(output)
logoutput=("grep -i completed /var/log/FirmwareUpgrade/"+output)
logout=commands.getoutput(logoutput)
print(logout)
os.system("cat /var/log/FirmwareUpgrade/"+output)
if "completed" in logout:
        print("Deployment done succesfully")
else:
        print("Deployment failed")
auditfile=('ls /var/tmp | grep -i .html')
audithtml=commands.getoutput(auditfile)
if audithtml.strip():
    print("html audit file is present in the given path")
    auditfileerror=("grep -i error /var/tmp/"+audithtml)
    auditerrorcount=commands.getoutput(auditfileerror)
    if "error" in auditerrorcount:
        print("There are errors in the audit file")
    else:
        print("No errors reported")
else:
    print("ERROR: No html audit file is present")
time.sleep(300)
sys.exit()


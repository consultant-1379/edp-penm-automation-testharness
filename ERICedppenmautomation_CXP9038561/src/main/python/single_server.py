#!/usr/bin/python
import pexpect
import time
import os
import commands
import sys
timeout=1800
# This script is used for the single server upgrade (MS upgrade)
for files in os.walk("/opt/ericsson/firmwareupgradetool/template/"):
    if files=="my_template":
        print("The sumtool is present in the specified directory")
os.system("touch top_output.txt")
os.system("top -b -n 1&>>top_output.txt")
print("waiting5minutes")
time.sleep(300)
print("executing script")
child=pexpect.spawn("python /opt/ericsson/firmwareupgradetool/firmware_upgrade.py --single --sedfile='/opt/ericsson/firmwareupgradetool/template/my_template' --username='root' --serverip='10.45.225.210' --noreboot")
print("paswdprompt")
child.expect("Enter the Sudo user password:")
child.sendline("shroot12")
print("sentpasswd")
time.sleep(1800)
os.chdir("/var/log/FirmwareUpgrade/")
cmd="ls -lrt enm_fw_upg_* | tail -1 |awk -F\" \" '{print $9}'"
output=commands.getoutput(cmd)
print(output)
os.system("cat /var/log/FirmwareUpgrade/"+output)
logoutput=("grep -i completed /var/log/FirmwareUpgrade/"+output)
logout=commands.getoutput(logoutput)
print(logout)
if "completed" in logout:
        print("Firmware upgrade successfull")
else:
        print("Upgrade failed")
time.sleep(300)
sys.exit()


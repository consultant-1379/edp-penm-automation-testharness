#!/usr/bin/python
import pexpect
import os
import time
import commands

os.chdir("/var/log/FirmwareUpgrade/")
cmd="ls -lrt single_server_upgrade_* | tail -1 |awk -F\" \" '{print $9}'"
output=commands.getoutput(cmd)
print output

cmd="ls -lrt configure_firmware_repo_* | tail -1 |awk -F\" \" '{print $9}'"
output1=commands.getoutput(cmd)
print output1

#child=pexpect.spawn("grep -E \'ERROR|WARNING|FAILURE' "+output)
#child=pexpect.spawn("grep -E \'ERROR|WARNING|FAILURE\' configure_firmware_repo_%H_%M_%d_%m_%Y.log")
#fout = file('errorfile.txt','a+')
#child.logfile = fout
#child.expect(pexpect.EOF)


cmd="grep -E \'ERROR|WARNING|FAILURE' "+output
b=commands.getoutput(cmd)
cmd="grep -E \'ERROR|WARNING|FAILURE' "+output1
c=commands.getoutput(cmd)
outfile = open('errorfile.txt','a')
print >> outfile, b
print >> outfile, c
outfile.close()


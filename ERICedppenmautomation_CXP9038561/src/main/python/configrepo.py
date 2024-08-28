#!/usr/bin/python
import pexpect
import time
import os
import commands
isog9="ls /var/tmp/ | grep .iso"
isofileg9=commands.getoutput(isog9)
isog8="ls /var/ | grep .iso"
isofileg8=commands.getoutput(isog8)
child=pexpect.spawn("python /opt/ericsson/firmwareupgradetool/firmware_upgrade.py --configure_repo --hpesppiso='/var/tmp/"+isofileg9+"' --postspp='yes' --postsppiso='/var/"+isofileg8+"' --brocade='no' ")
child.expect(pexpect.EOF)
output = child.before
print output

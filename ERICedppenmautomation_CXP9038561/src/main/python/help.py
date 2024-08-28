#!/usr/bin/python
import os
os.system("python /opt/ericsson/firmwareupgradetool/firmware_upgrade.py --help >>help_output.txt")
os.system("cat help_output.txt")
file = open("help_output.txt","r")
filelist = file.readlines()
for line in file:
   print(line)
   if str("firmware_upgrade_cli.py") in line:
      print("The help option is printed suncesfully")
file.close()
os.system("rm -rf help_output.txt")
#os.system("rm -rf help_output.txt")
   # else:
   #     print("failed to print the help output")


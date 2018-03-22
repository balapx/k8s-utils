#!/usr/bin/env python

import paramiko
import random

cmd = "ls"
host = "70.0.0.40"
vms = ['TEST-PX_LW_555-20180318-173838-2','TEST-PX_LW_555-20180318-173838-3','TEST-PX_LW_555-20180318-173838-4','TEST-PX_LW_555-20180318-173838-5','TEST-PX_LW_555-20180318-173838-6','TEST-PX_LW_555-20180318-173838-7','TEST-PX_LW_555-20180318-173838-8','TEST-PX_LW_555-20180318-173838-9']

def reboot_vm(vms, num):
    for x in range(num):
        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.WarningPolicy())

            client.connect(host, port=22, username="root", password="Password1")
            cmd = "VBoxManage controlvm " + vms[0] + " poweroff"
            stdin, stdout, stderr = client.exec_command(cmd)
            cmd = "VBoxManage controlvm " + vms[0] + " restart"
            stdin, stdout, stderr = client.exec_command(cmd)
            print stdout.read(),

            finally:
                client.close()
    return 0

#random.shuffle(vms)
#print(vms)
reboot_vm(vms, 1)

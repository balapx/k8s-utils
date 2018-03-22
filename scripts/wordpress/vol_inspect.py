#!/usr/bin/python

import time
import subprocess
import random

def get_vol():
    cmd = "/opt/pwx/bin/pxctl v l | grep [0-9] | awk '{print $1}'"
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    #print "Command output : ", output
    #print "Command exit status/return code : ", p_status
    vols = output.split('\n')
    return vols

def vol_inspect(vols, num):
    for x in range(num):
        for z in range(len(vols)):
            cmd = "/opt/pwx/bin/pxctl -j v i " + vols[z]
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
            (output, err) = p.communicate()
            p_status = p.wait()
     	    #print "Command exit status/return code : ", p_status
            print(output)

for x in range(1):
    vols = get_vol()
    vol_inspect(vols, 1)

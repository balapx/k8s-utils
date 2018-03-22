#!/usr/bin/python

import os
import time
import subprocess

def get_px():
    cmd = "kubectl get pods -n=kube-system -l name=portworx | grep portworx | shuf | awk '{print $1}'"
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    #print "Command output : ", output
    #print "Command exit status/return code : ", p_status

    px_nodes = output.split('\n')
    print(px_nodes)
    return px_nodes

def reboot_px(px_nodes, num):
    for x in range(num):
        cmd = "kubectl delete pods " + px_nodes[x] + " " + "-n=kube-system"
        print(cmd)
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p_status = p.wait()
 	print "Command exit status/return code : ", p_status

def wait_px():
    count = 0
    cmd = "kubectl get pods -n=kube-system -l name=portworx | grep portworx | awk '{print $2}' | grep 1/1 | wc | awk '{print $1}'"
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    print(output)
    while (output == 8 and count == 20):
        print('{} : Sleeping for 30 sec'.format(count))
        time.sleep(30)
        cmd = "kubectl get pods -n=kube-system -l name=portworx | grep portworx | awk '{print $2}' | grep 1/1 | wc | awk '{print $1}'"
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p_status = p.wait()
        print(output)
        count = count + 1
    if count != 20:
        print("PX is up and running on all nodes")
        return 0
    else:
        print("PX is not up and running on all nodes")
        exit()

def verify_wp():
    cmd = "kubectl get pods --all-namespaces | grep wordpress | wc | awk '{print $1}'"
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    return(output)

for x in range(50):
    px_nodes = get_px()
    reboot_px(px_nodes, 3)
    time.sleep(30)
    print(wait_px())
    time.sleep(30)
    wp_num = verify_wp()
    print(wp_num)
    if int(wp_num) == 120:
        print('{} : Iteration PASSED'.format(x))
    else:
        print('{} : Iteration FAILED'.format(x))
        exit()

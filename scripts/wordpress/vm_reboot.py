#!/usr/bin/python

import time
import subprocess
import random

def get_vm():
    cmd = "aws ec2 describe-instances --filters Name=instance-type,Values=t2.2xlarge  --query Reservations[].Instances[].InstanceId"
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    #print "Command output : ", output
    #print "Command exit status/return code : ", p_status
    
    output = output.replace('[', "")
    output = output.replace(']', "")
    output = output.replace(',', "")
    output = output.replace('\n', "")
    output = output.replace('    ', "")
    output = output.replace('"', "")
    vm_nodes = output.split(' ')
    vm_nodes.remove('i-05fe8a4652d72e2d0')
    vm_nodes.remove('i-040c9297307dfcf9d')
    return vm_nodes

def reboot_vm(px_nodes, num):
    for x in range(num):
        cmd = "aws ec2 reboot-instances --instance-ids " + px_nodes[x]
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

    count = 0
    while int(output) < 9:
        print('{} : Sleeping for 30 sec'.format(count))
        time.sleep(10)
        cmd = "kubectl get pods -n=kube-system -l name=portworx -o wide | grep portworx | awk '{print $2}' | grep 1/1 | wc | awk '{print $1}'"
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p_status = p.wait()
        print(output)
        count = count + 1
    print("PX is up and running on all nodes")
    return output

def verify_wp():
    cmd = "kubectl get pods --all-namespaces | grep wordpress | grep Running | wc | awk '{print $1}'"
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    print(output)

    count = 0
    while int(output) < 220:
        print('{} : Sleeping for 30 sec'.format(count))
        time.sleep(10)
        cmd = "kubectl get pods --all-namespaces -o wide | grep wordpress | grep Running |  wc | awk '{print $1}'"
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p_status = p.wait()
        print(output)
        count = count + 1
    print("All Wordpress pods are up and running")
    return output


for x in range(50):
    px_nodes = get_vm()

    # shuffle the nodes that needs to be rebooted
    vm_nodes_shuf = random.sample(px_nodes, len(px_nodes))
    print(vm_nodes_shuf)

    reboot_vm(vm_nodes_shuf, 4)
    time.sleep(100)
    print(wait_px())
    wp_num = verify_wp()
    if int(wp_num) == 220:
        print('{} : Iteration PASSED'.format(x))
    else:
        print('{} : Iteration FAILED'.format(x))
    time.sleep(600)

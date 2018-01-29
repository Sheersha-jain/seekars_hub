#!/usr/bin/python

import socket,commands,time,os

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.bind(("192.168.1.200",8002)) ## bind port with server system IP

name,name1=s.recvfrom(100)  ## recevice value from client side
size,size1=s.recvfrom(100)  ## recevice value from client side

commands.getoutput("lvcreate --name "+name+" --size "+size+" myvg") ## create logical volume 

commands.getoutput("yum install -y scsi-target-utils") ## install iscsi packages

f=open('/etc/tgt/targets.conf','w+')  ## write configuration file

f.write("<target "+name+"> \n")
f.write("backing-store /dev/myvg/"+name+" \n")
f.write("</target>")
f.close()
time.sleep(2)  ## sleep for 2 seconds

commands.getoutput("service tgtd restart") ## start block storage service

commands.getoutput("iptables -F;  setenforce   0") ## disable firewall and selinux policy




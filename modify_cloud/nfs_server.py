#!/usr/bin/python

import socket,commands,os,time

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.bind(("192.168.1.200",8001)) ## bind 8001 port on server

name,name1=s.recvfrom(100) ## recevice name variable value from client machine
size,size1=s.recvfrom(100) ## recevice size variable value from client machine

commands.getoutput("lvcreate --name "+name+" --size "+size+" myvg") ## create logical volume
commands.getoutput("mkfs.ext4 /dev/myvg/"+name) ## format logical volume
commands.getoutput("mkdir /mnt/"+name)  
commands.getoutput("mount /dev/myvg/"+name+"  /mnt/"+name) ## mount logical volume

commands.getoutput("yum install nfs-utils -y")  ## instll nfs packges

f=open('/etc/exports', 'w+') ## write nfs config file  
f.write("/mnt/"+name+"  *(rw,no_root_squash)")
f.close()

commands.getoutput("service nfs restart")  ## restart nfs service
commands.getoutput("exportfs -r") ## reload nfs config file 
commands.getoutput("iptables -F;  setenforce   0") ## disable firewall and selinux policy




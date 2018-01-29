#!/usr/bin/python

import socket,commands,os,time

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.bind(("192.168.1.200",8001)) ## bind port with server system IP

name,name1=s.recvfrom(100)  ## recevice value from client side

size,size1=s.recvfrom(100)  ## recevice value from client side

#print  name
#print  size

commands.getoutput("lvcreate --name "+name+" --size "+size+" myvg") ## create logical volume

commands.getoutput("mkfs.ext4 /dev/myvg/"+name) ## format created logical volume
commands.getoutput("mkdir /mnt/"+name) ## create folder for mounting object storage
commands.getoutput("mount /dev/myvg/"+name+"  /mnt/"+name) ## mount logical volume 
commands.getoutput("yum install nfs-utils -y")   ## install nfs utils packages
f=open('/etc/exports', 'w+') ## write exports files
f.write("/mnt/"+name+"  *(rw,no_root_squash)") 
f.close()

commands.getoutput("service nfs restart") ## restarting nfs service 
commands.getoutput("exportfs -r") ## reload nfs config file

commands.getoutput("iptables -F;  setenforce   0") ## disable firewall and selinux policy




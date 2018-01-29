#!/usr/bin/python2


import socket,commands,os,time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

name=raw_input("enter the name storage : ")
size=raw_input("enter the size : ")

s.sendto(name,("192.168.1.200",8002)) ## send name variable value to nfs sever on port 8002
s.sendto(size,("192.168.1.200",8002))  ## send size variable value to nfs sever on port 8002

commands.getoutput("yum install -y iscsi-initiator-utils") ## install client side iscsi package

time.sleep(10)

os.system("iscsiadm --mode node --targetname "+name+" --portal 192.168.1.200:3260 --logout" ) ##logout old session
 
os.system("iscsiadm --mode discoverydb --type sendtargets --portal 192.168.1.200 --discover") ## Discover IQN Number
os.system("iscsiadm --mode node --targetname "+name+" --portal 192.168.1.200:3260 --login" )  ## Login into target  
commands.getoutput("iptables -F;  setenforce   0") ## disable firewall and selinux policy

execfile('staas.py') ## returnning to main file


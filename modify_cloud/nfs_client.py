#!/usr/bin/python2


import socket,commands,os,time

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

name=raw_input("enter the name of storage: ")  ## Ask storage name from client 

size=raw_input("enter the size of storage: ")  ## Ask size of storage from client

s.sendto(name,("192.168.1.200",8001))  ## send name variable value to nfs sever on port 8001
s.sendto(size,("192.168.1.200",8001))  ## send size variable value to nfs sever on port 8001

commands.getoutput("mkdir /media/"+name ) 
time.sleep(10) ## sleep for 10 seconds

os.system("showmount -e 192.168.1.200")  ## this will show sharing path of nfs server
os.system("mount 192.168.1.200:/mnt/"+name+"  /media/"+name) ## mounting object storage on client side
commands.getoutput("iptables -F;  setenforce   0") ## disable firewall and selinux policy
execfile('staas.py') ## returing to storage script 

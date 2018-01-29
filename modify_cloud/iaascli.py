#!/usr/bin/python2


import socket,commands,os,time

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

x="""
print  "IAAS  cloud is loading  !_________"
print   "Wait for Os available Here !!!!!!! "
print   "Press  1  For ubuntu 14.04  os __ : "
print   "Press  2  For Mint OS    os __ : "
print   "Press  3  For Fedora  Os  __ : "
"""

print  x

ich=raw_input()

if  ich ==  '1' :
	s.sendto(ich,("192.168.1.200",3322))
	execfile('iaas_build.py')
elif ich ==  '2' :
	s.sendto(ich,("192.168.1.200",3322))
	execfile('iaas_build.py')
elif   ich ==  '3' :
	s.sendto(ich,("192.168.1.200",3322))
	execfile('iaas_build.py')

else :
	print   "Wrong choice"
	print   "returning  to main Menu !!  "
	execfile('start.py')




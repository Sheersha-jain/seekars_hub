#!/usr/bin/python2


import  time,sys,commands,os,socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

x="""
print  	"Welcome to Cloud  Services !!!!!!!!   "
print   "Press 1  For Object storage Access   _____   :  "
print   "Press 2  For Block storage  Access   _____   :  "
"""

print  x
ch=raw_input()

if  ch  ==  '1'  :  ## checking choice number 
	execfile('nfs_client.py')  ## run nfs_client script file
	execfile('start.py')  ## run main file

elif   ch  ==  '2' :  ## checking choice number 
	execfile('iscsi_client.py')  ## run iscsi_client script file 
	execfile('start.py')  ## run main file 
else :
	print  	"You have entered wrong option "
	print   "closing the program "
	print   "Returning to main menu ___"
	execfile('start.py') ## run main file







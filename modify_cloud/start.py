#!/usr/bin/python2


import  time,sys,commands,os,socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

x="""
print  "Welcome to CLoud  SErvices !!!!!!!!   "
print   "Press 1  For SAAS  Cloud Access   _____   :  "
print   "Press 2  For StAAS Cloud Access   _____   :  "
print   "Press 3  For IAAS  Cloud Access   _____   :  "
"""

print  x
ch=raw_input()

if  ch  ==  '1'  :
	execfile('saas.py')  		## run software as a service python script

elif   ch  ==   '2'  :
	execfile('staas.py')		## run storage as a service python script

elif   ch  ==  '3' :
	execfile('iaascli.py')		## run IAAS python script
else :
	print  "wrong option "
	print  "closing the program "
	print  "if you want to access please run again this file !!___"







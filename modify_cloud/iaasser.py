#!/usr/bin/python2


import socket,commands
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("192.168.1.200",3322))

while True   :
	choice=s.recvfrom(100)[0]
	ros=s.recvfrom(100)
	rram=s.recvfrom(100)
	rcpu=s.recvfrom(100)
	rhd=s.recvfrom(100)
	os=ros[0]
	ram=rram[0]
	cpu=rcpu[0]
	hd=rhd[0]

	if  choice ==  '1' :

		commands.getoutput("virt-install --name "+os+" --ram "+ram+" --vcpu "+cpu+" --cdrom /var/ftp/pub/ubuntu.iso --nodisk")
	elif  choice  ==  '2'  :
		commands.getoutput("virt-install --name "+os+" --ram "+ram+" --vcpu "+cpu+" --cdrom /var/ftp/pub/mint.iso --nodisk")
	elif  choice ==  '3'  :
		commands.getoutput("virt-install --name "+os+" --ram "+ram+" --vcpu "+cpu+" --cdrom /var/ftp/pub/fedora.iso --nodisk")

	else :
		print    "Wrong choice  "
		


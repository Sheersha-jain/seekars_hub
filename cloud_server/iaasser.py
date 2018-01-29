#!/usr/bin/python2


import socket,commands,time,commands,os ## Import Libraries

os.system('yum   install  libvirt virt-manager  qemu-kvm  -y   &>/dev/null')  ## Install Virtualization Packages
os.system('service  libvirtd  restart   &>/dev/null')  ## Restart libvirt service
os.system('iptables  -F ; setenforce 0') ## Stop firewall and selinux policy


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(("192.168.1.200",3322)) ## bind port with server system IP 


while True   :
	choice=s.recvfrom(100)[0]
	ros=s.recvfrom(100)
	rram=s.recvfrom(100)
	rcpu=s.recvfrom(100)
	rhd=s.recvfrom(100)
	os1=ros[0]
	ram=rram[0]
	cpu=rcpu[0]
	hd=rhd[0]
	#print  type(choice)
	#print  os1
	#print  type(ram)
	#print  cpu
	#print  hd

	if  choice ==  '1' :

		os.system("virt-install --name "+os1+" --ram "+ram+" --vcpu "+cpu+" --cdrom /var/ftp/pub/ubuntu.iso --nodisk")
	
	elif  choice  ==  '2'  :
		
		os.system("virt-install --name "+os+" --ram "+ram+" --vcpu "+cpu+" --cdrom /var/ftp/pub/mint.iso --nodisk")
	
	elif  choice ==  '3'  :
			
		os.system("virt-install --name "+os+" --ram "+ram+" --vcpu "+cpu+" --cdrom /var/ftp/pub/fedora.iso --nodisk")

	else :
		print    "Wrong choice  "
		


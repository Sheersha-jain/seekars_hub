import socket,commands
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("192.168.0.201",3222))
while 3<4:
	ros=s.recvfrom(100)
	rram=s.recvfrom(100)
	rcpu=s.recvfrom(100)
	rhd=s.recvfrom(100)
	os=ros[0]
	ram=rram[0]
	cpu=rcpu[0]
	hd=rhd[0]
        print os
	commands.getoutput("virt-install --name "+os+" --ram "+ram+" --vcpu "+cpu+"--vnc --vncport=5903 --vnclisten=192.168.0.201--location ftp://192.168.0.201/pub/rhel6 --disk path=/var/lib/libvirt/images/"+os+".img,size="+hd+" --extra-args ks=ftp://192.168.0.201/pub/ks.cfg ")
	


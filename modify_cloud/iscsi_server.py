import socket,commands
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.bind(("192.168.0.201",8002)) ## bind 8002 port on server

name,name1=s.recvfrom(100) ## recevice name variable value from client machine
size,size1=s.recvfrom(100) ## recevice size variable value from client machine

commands.getoutput("lvcreate --name "+name+" --size "+size+" myvg") ## create logical volume
commands.getoutput("yum install -y scsi-target-utils") ##install iscsi packages

f=open('/etc/tgt/targets.conf','w+') ## write target config file 
f.write("<target "+name+"> \n")
f.write("backing-store /dev/myvg/"+name+" \n")
f.write("</target>")
f.close()

commands.getoutput("service tgtd restart") ## restart targer service 
commands.getoutput("iptables -F;  setenforce   0") ## disable firewall and selinux policy


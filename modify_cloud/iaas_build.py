#!/usr/bin/python

import  os,socket,time,commands,sys

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


os_name=raw_input("enter os name : ")
ram=raw_input("enter ram in MB : ")
cpu=raw_input("enter cpu : ")
hard_disk=raw_input("enter hard disk in GB : ")
s.sendto(os_name,("192.168.1.200",3322))
s.sendto(ram,("192.168.1.200",3322))
s.sendto(cpu,("192.168.1.200",3322))
s.sendto(hard_disk,("192.168.1.200",3322))

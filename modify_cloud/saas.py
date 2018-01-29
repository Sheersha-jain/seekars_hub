#!/usr/bin/python2


import  time,sys,os,commands

x="""
print  "Press 1  for  Firefox  :  "
print  "Press 2  for  Calculator  :  "
print  "Press 1  for  Text Editor  :  "
"""

print  x
fch=raw_input()

if  fch ==  '1' :  			## checking choice number
	execfile('fire.py')   	## run firefox script
	execfile('saas.py')		## run main script

elif  fch  ==  '2'  :			## checking choice number
	execfile('calcu.py')		## run firefox script
	execfile('saas.py')		## run main script

elif   fch ==  '3'  :			## checking choice number
	execfile('gedit.py')		## run firefox script
	execfile('saas.py')		## run main script

else :
	print  "Wrong Option "
	time.sleep(2)
	execfile('start.py')		## run main script




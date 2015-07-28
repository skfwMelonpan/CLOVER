#!/usr/bin/python

import sys
import serial
import time
import datetime

ser=serial.Serial("/dev/ttyAMA0",9600)

start = datetime.datetime.now()
end = start+datetime.timedelta(seconds=60)

print start

while True:
	line=ser.readline()
	print "%s,%s"%(datetime.datetime.now()-start,line)
	if end-datetime.datetime.now()<datetime.timedelta(seconds=0):
		sys.exit(0)
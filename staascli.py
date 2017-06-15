#!/usr/bin/python
import os,socket,time

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s_ip="192.168.122.254"
s_port=7777

#it contains the storage name
drive_name=raw_input("enter storage drive name: ")
#it stores the required storage size
drive_size=raw_input("enter required storage size like 1M or 1G: ")
#now sending the name and size of storage
s.sendto(drive_name,(s_ip,s_port))
s.sendto(drive_size,(s_ip,s_port))


res=s.recvfrom(4)
if res[0]=="done":
	#making directory in media to create mount
	os.system('mkdir /media/' + drive_name)
	#mounting the drive
	os.system('mount ' + s_ip + ':/mnt/' + drive_name + ' /media/' + drive_name)
else:
	print "no response from  storage cloud"


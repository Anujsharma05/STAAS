#!/usr/bin/python
import os,socket,time

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",7777))

#receiving storage drive name and size
#data will stores the drive_name
data=s.recvfrom(100)
d_name=data[0]
#data1 will store the drive size
data1=s.recvfrom(100)
d_size=data1[0]
#cliaddr stores ip of client
cliaddr=data[1][0]

#creating LVM by name of client drive
os.system('lvcreate --name ' + d_name + ' --size ' + d_size + 'M mydevice')
#now time to format client drive with ext4 
os.system('mkfs.ext4 /dev/mydevice/' + d_name)
#now creating mount point
os.system('mkdir /mnt/' + d_name)
#now mounting drive locally 
os.system('mount /dev/mydevice/' + d_name + ' /mnt/' + d_name)
#now time to configure nfs server
#os.system('yum install nfs-utils -y')

#making entry in NFS export fiel
entry="/mnt/"+d_name+ " " + cliaddr + "(rw,no_root_squash)"
#appending the entry variable to /etc/exports file
f=open('/etc/exports','a')
f.write(entry)
f.write("\n")
f.close()
#finally starting NFS service along with using error code
check=os.system('exportfs -r')
#checking error code
if check==0:
	s.sendto("done",data[1])
else:
	print "please check your code"

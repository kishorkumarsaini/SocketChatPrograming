#!/usr/bin/python3
import socket
import time
import threading



rev_ip='127.0.0.1'
rev_port=10022
#***************************
send_ip='127.0.0.1'
send_port=10033
#iv4 family  and UDP==============
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind((rev_ip,rev_port))

def  receriver():
	while 4>2:
		clinet=s.recv(1000).decode('utf-8')
		print("sender message=",clinet)

		

def sender():		
	while 4>2:
		msg=input("enter the message to send=")
		s.sendto(msg.encode('utf-8'),(send_ip,send_port))
		#time.sleep(10)


threading.Thread(target=receriver).start()
threading.Thread(target=sender).start()

while True:
	pass
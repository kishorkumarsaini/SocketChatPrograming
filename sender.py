#!/usr/bin/python3
import socket
import time
import threading

#iv4 family  and UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
send_ip='127.0.0.1'
send_port=10033

def senderCode():
	while True:
		msg=input("enter a message to send=")
		s.sendto(msg.encode('utf-8'),("127.0.0.1",10022))
		#time.sleep(10)
	
s.bind((send_ip,send_port))

def clientCode():
	while True:
		clinet=s.recv(1000).decode('utf-8')
		print("receiver message=",clinet)
		#time.sleep(10)
	
threading.Thread(target=senderCode).start()
threading.Thread(target=clientCode).start()

while True:
	pass
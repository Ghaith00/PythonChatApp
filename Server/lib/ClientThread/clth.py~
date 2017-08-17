#!/usr/bin/env python
# (C) coded by Tabib Ghaith 

import socket
import threading

class ClientThread(threading.Thread):
	def __init__(self, ip, port, clientsocket,Buffer,user_list,listclient):
		threading.Thread.__init__(self)
		self.ip = ip
		self.port = port
		self.clientsocket = clientsocket
		self.Buffer = Buffer
		self.listclient = listclient
		# get username 
		self.user = self.clientsocket.recv(1024)
		self.user_list = user_list		
		self.user_list.append(self.user)
		
	def run(self):
		self.Buffer.append( "\n[+] Connection from " +str(self.ip)+" : "+str(self.port))  
		while True :
			# recv message from user
			data = ''
			data = self.clientsocket.recv(1028)
			# analysing data
			if len(data) == 0:
				self.Buffer.append( "\n[-] "+str(self.user)+"("+str(self.ip)+str(self.port)+") deconnected")
				self.listclient.remove(self.clientsocket)
				self.user_list.remove(self.user)
				self.clientsocket.close()
				break
			self.Buffer.append("\n"+str(self.user)+" >> "+str(data))
			self.send_all(str(self.user)+" >> "+data) 
	def send_all(self,data):
		for client in self.listclient :
			if id(client) != id(self.clientsocket) :
				client.send(data)

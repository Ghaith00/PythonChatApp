#!/usr/bin/python
# (C) coded by Tabib Ghaith

import socket
import threading
import ClientThread.clth as cl

#------------------------------------------------------------------------------------------------------#
class Server(object):

	def __init__(self, port=4141, user_list=[]):
		self.user_list = user_list
		# prepare the socket
		self.port  =  port
		self.sock = socket.socket()# standard TCP protocole
		self.sock.bind(("",self.port))
		self.listclient = []

	def start(self):
		# let's begin !
		print '[.] Server Started !'
		user_id = 0
		while True :
			# waiting for client
			self.sock.listen(10)
			# accept him no password la walou (make a socket for him )
			(client, (ip,port)) =self.sock.accept()
			# store the client socket so after we can closed in case of
			self.listclient.append(client)
			user_id = user_id + 1

			# let the thread handel him so we can accept more
			thread = cl.ClientThread(ip, port, client, self.user_list, self.listclient)
			thread.start()

	def deconnectall(self):
		# close all socket
		for client in self.listclient :
			client.shutdown(socket.SHUT_WR)
			client.close()

	def release_listen(self):
		# listening socket please stop
		socket.socket().connect( ('127.0.0.1', self.port))
		self.deconnectall()
		self.sock.close()
	def stop(self):
		global end
		# in case button exit used
		end = True
		self.deconnectall()
		self.release_listen()

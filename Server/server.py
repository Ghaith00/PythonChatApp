#!/usr/bin/python
# (C) coded by Tabib Ghaith 

import socket
import threading
import serverinterface.graphique
import ClientThread.clth 
#-------------------Global Vars-----------------------------------------------------------------------#
end = False
Buffer = []
user_list = []

#------------------------------------------------------------------------------------------------------#	
	
class ServingClient(threading.Thread):
	
	def __init__(self):
		threading.Thread.__init__(self)
		# prepare the socket
		self.port  =  5000
		self.sock = socket.socket()# standard TCP protocole
		self.sock.bind(("",self.port))
		self.listclient = []
		
	def run(self):
		global end
		# let's begin !
		Buffer.append("server started \n-------------------------------------------")
		user_id = 0
		while True :
			# waiting for client
			self.sock.listen(10)
			# accept him no password la walou (make a socket for him )
			(client, (ip,port)) =self.sock.accept()
			# store the client socket so after we can closed in case of
			self.listclient.append(client)
			user_id = user_id + 1
			if end : break
			# let the thread handel him so we can accept more
			thread = ClientThread.clth.ClientThread(ip,port,client,Buffer,user_list,self.listclient)
			thread.start()
	
	def deconnectall(self):
		# close all socket
		for client in self.listclient :
			client.shutdown(socket.SHUT_WR)
			client.close()
	
	def release_listen(self):
		# listening socket please stop
		socket.socket().connect( ('127.0.0.1',5000))
		self.deconnectall()
		self.sock.close()
	def stoping(self):
		global end
		# in case button exit used
		end = True
		self.deconnectall()
		self.release_listen()
		
#------------------------ the main -----------------------#
def Main():

	
	# creating the server socket thread 
	mainthread = ServingClient()
	# creating the app 
	Myapp = serverinterface.graphique.app(Buffer,user_list,mainthread.stoping)
	mainthread.start()
	
	# looping our window
	Myapp.loop()
	
	
	# do a looping (bouclage 127.0.0.1) to release the listening in case of the user press x (not exit button)
	mainthread.stoping()
	mainthread.join()
if __name__ == '__main__':
	Main()
	

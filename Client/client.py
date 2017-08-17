#!/usr/bin/env python
# (C) coded by Tabib Ghaith
import socket
import threading
from ClientInterface.graphique import *
class Connect(threading.Thread):

	def __init__(self,sock):
		threading.Thread.__init__(self)
		# prepare the socket
		self.host = '127.0.0.1'
		self.port  =  4141
		self.sock = sock
		self.recvthread = threading.Thread(target=self.recv_data)
	def run(self):
		# let's begin !
		Buffer.append("Connected To server "+str(self.host)+"\n-------------------------------------------")
		# start a receving thread

		self.recvthread.start()
		self.recvthread.join()
	def send(self,msg):
		self.sock.send(msg)
		Buffer.append("\nme >> "+str(msg))
	def recv_data(self):
		while True:
			# ready to receives
			msg = self.sock.recv(1028)
			if len(msg) == 0  :
				Buffer.append("\nConncetion lost")
				break
			Buffer.append("\n"+str(msg))
		self.sock.close()
	def stoping(self):
		self.sock.shutdown(socket.SHUT_WR)
def conn(username):
	sock = socket.socket()# standard TCP protocole

	if sock.connect_ex(('127.0.0.1',4141)) == 0 :
		sock.send(username)
		return [True , sock ]
	else :
		sock.close()
		return [False , -1]

def Main():
	global Buffer
	Buffer = []
	# set user name and the server ip and port
	login = log(conn)
	login.loop()
	MainSocket = login.sock
	#
	if MainSocket is not None :
		user = Connect(MainSocket)
		user.start()
		fen = app(Buffer,user.stoping,user.send)
		fen.loop()
		user.stoping()

if __name__ == '__main__':
		Main()

#!/usr/bin/env python
# (C) coded by Tabib Ghaith 

from Tkinter import * 
import ttk
import threading
import time
import socket
def stop(stoping):
	# Stop the mainthread && releasing listening socket
	stoping()
	time.sleep(1)
	exit(0)
def start(login,stoping,Buffer,console):
	login.append(1)
	data_update(Buffer,console,stoping)
def data_update(Buffer,console,stoping):
	# empty the buffer into the console text (refresh every 0.5ms)
	if Buffer != []:
		console.config(state=NORMAL)
		console.insert('end',Buffer[0])
		console.config(state=DISABLED)
		Buffer.remove(Buffer[0])
	console.after(500, data_update,Buffer,console,stoping)
def send_data(send,msg):
	send(msg)
class app(object):
	def __init__(self,Buffer,stoping,send):
		# creating out main window  (root)
		self.root = Tk()
		self.root.title('User Interface')
		# creating the console and scrollbar
		self.console = Text(self.root,width=50,height=20,wrap='word',state=DISABLED,bg="white")
		self.console.grid(row = 0 , column=0,padx=1,pady=1,columnspan=1)
		self.scrollbar = ttk.Scrollbar(self.root,orient = VERTICAL ,command=self.console.yview)
		self.scrollbar.grid(row = 0 , column=2,sticky ='ns')
		self.console.config(yscrollcommand = self.scrollbar.set)
		data_update(Buffer,self.console,stoping)
		# send division 
		self.entree = ttk.Entry(self.root, width=44)
		self.entree.grid(row = 1 , column=0,columnspan=2)
		self.button0 = ttk.Button(self.root, text ='Send',command=lambda:send_data(send,self.entree.get()))
		self.button0.grid(row = 1 , column=3)
		
		
		
		self.button2 = ttk.Button(self.root, text ='    Exit    ',command=lambda: stop(stoping)).grid(row = 1 , column=4)
		
	# keep the window opened
	def loop(self):
		self.root.mainloop()
class log(object):
	def __init__(self,conn):
		# creating out main window  (root)
		self.root = Tk()
		self.root.title('Login')
		self.conn = conn
		# login division
		Label(self.root,text="User Name :").grid(row=0,column=0,pady='0.1i',padx='0.1i')
		self.entree = ttk.Entry(self.root, width=20)
		self.entree.grid(row = 0 , column=1,columnspan=1,pady='0.1i',padx='0.1i')
		self.button0 = ttk.Button(self.root, text ='Connect',command=lambda:self.log_user(self.entree.get() ))
		self.button0.grid(row = 1 , column=0,columnspan=2,pady='0.1i')
		self.sock = None
	
	def loop(self):
		self.root.mainloop()
	def log_user(self,username):
		Status =  self.conn(username)
		if Status[0]:
			self.sock = Status[1]
			self.root.destroy()
			self.root.quit()
		else :
			Label(self.root,text="Server not found",bg="white").grid(row=2,column=0,columnspan=3)
			
			

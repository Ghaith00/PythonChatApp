#!/usr/bin/env python
# (C) coded by Tabib Ghaith 

from Tkinter import * 
import ttk
import threading
import time
def add_user(user_name,myapp):
	myapp.liste.insert(END, user_name)
	
def stop(stoping):
	# Stop the mainthread 
	stoping()
	# wait until all the threads are over max 1s
	time.sleep(1)
	exit(0)
def data_update(Buffer,console,user_list,liste,stoping):
	# empty the buffer into the console text (refresh every 0.5ms)
	if Buffer != [] :
		console.config(state=NORMAL)
		console.insert('end',Buffer[0])
		console.config(state=DISABLED)
		del Buffer[0]
	# update user list
	liste.delete(0, END)
	for user in user_list :
		liste.insert(END, user)
	console.after(500, data_update,Buffer,console,user_list,liste,stoping)
class app(object):
	def __init__(self,Buffer,user_list,stoping):
		# creating out main window  (root)
		self.root = Tk()
		self.root.title('Server')
		# creating the console and scrollbar
		self.console = Text(self.root,width=50,height=20,wrap='word',state=DISABLED,bg="white")
		self.console.grid(row = 0 , column=0,padx=1,pady=1)
		self.scrollbar = ttk.Scrollbar(self.root,orient = VERTICAL ,command=self.console.yview)
		self.scrollbar.grid(row = 0 , column=1,sticky ='ns')
		self.console.config(yscrollcommand = self.scrollbar.set)
		# user list
		self.liste = Listbox(self.root,bg="white")
		self.liste.grid(row = 0 , column=2,columnspan=2,sticky=W+E+N+S,)
		# button start server and exit
		self.button1 = ttk.Button(self.root, text ='Start Server',command=lambda: data_update(Buffer,self.console,user_list,self.liste,stoping))
		self.button1.grid(row = 1 , column=2)
		self.button2 = ttk.Button(self.root, text ='    Exit    ',command=lambda: stop(stoping)).grid(row = 1 , column=3)
		
	# keep the window opened
	def loop(self):
		self.root.mainloop()

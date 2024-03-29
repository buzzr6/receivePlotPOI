import socket
import time
import json
import matplotlib.pyplot as plt
import numpy as np
from threading import Thread
import traceback

UDP_IP_ADDRESS = "192.168.0.101"#"172.20.10.6"#"127.0.0.1"
UDP_PORT_NO = 1234

serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#serverSock.setblocking(0)
serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
serverSock.listen(5)

x = []
y = []
fig,ax=plt.subplots()

tmp=0
connected = False
timeout = time.time() + 60 * 60 #1 hour connection timeout
while time.time() < timeout:
	# Wait for connection
	while not connected and time.time() < timeout:
		try:
			print("Waiting for connection from client")
			conn,addr = serverSock.accept()
			connected = True
			print("Connection accepted from: ", addr)
			break;
		except socket.error:
			''''''
	
	# Accept messages
	if connected:
		try:
			# Receive message
			data = conn.recv(1024)
			msg = data.decode()
			print("Msg: ", msg)
			
			# Graceful exit condition
			if msg == "":
				break;
				
			# Retrieve coordinates from file
			gpsLogPath = "test.log" #TODO: adjust accordingly
			prev = ""
			with open(gpsLogPath, 'rb') as file:
				for line in file:
					penultimate = prev
					prev = line

			lat = float(str(penultimate).split('\\t')[-1].split('\\n')[0])
			lon = float(str(line).split('\\t')[-1].split('\\n')[0])

			for elem in [lat,lon]:
				print(elem)
			
			x.append(lon)
			y.append(lat)
			print("x:",x)
			print("y:",y)

			# Plot
			while tmp < len(x):
				tmp+=1
				plt.plot(x[0],y[0])
				plt.plot([],[])
				for i in range(0,tmp):
					plt.plot(x[i],y[i],'o')
				time.sleep(.5)
                # Now I have no idea why the following if/else has to be broken down like that,
                # but it seems to be the case, so probably best not to fuck with it
				if tmp==1:
					plt.savefig('C:\\Apache24\\htdocs\\plot.jpg')
                    #plt.show()
				else:
					plt.savefig('C:\\Apache24\\htdocs\\plot.jpg')
					#plt.show()#draw()
		except socket.error:
			# Will throw error every time no message is received...
			# This is fine, just continue looping
			'''traceback.print_exc()
			conn.close()
			break'''
	else:
		print("Timeout reached before connection established")

conn.close()
print("Done.")

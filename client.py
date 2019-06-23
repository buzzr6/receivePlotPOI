import socket
import cmd
import time

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6288

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

class Prompt(cmd.Cmd):
	def do_send(self,msg):
		print("Sending: <", msg, ">")
		clientSock.sendto(str.encode(msg), (UDP_IP_ADDRESS, UDP_PORT_NO))
	
	def default(self,msg):
		print("Sending: <", msg, ">")
		clientSock.sendto(str.encode(msg), (UDP_IP_ADDRESS, UDP_PORT_NO))

	def do_EOF(self, line):
		return True

if __name__ == '__main__':
	Prompt().cmdloop()
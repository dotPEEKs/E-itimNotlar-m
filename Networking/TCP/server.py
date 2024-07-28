import socket
import threading
import signal
from cmd import Cmd as cmd
class BindSocket:
	def __init__(self,ip,port):
		self.ip = ip
		self.port = port
		self.condition = True
		self.client_credentials = []
	def init_sock(self):
		print("Soket kuruldu: %s:%s" % (self.ip,self.port))
		self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
		self.socket.bind((self.ip,self.port))
		self.socket.listen(1)
		self.accept_connections()
	def socket_loop(self):
		while self.condition:
			try:
				 client_ip,client_sock = self.socket.accept()
				 print(client_ip,client_sock)
				 self.client_credentials.append(client_sock)
				 self.client_credentials.append(client_ip)
				 print("Bağlantı kabul edildi %s:%s" % (self.client_credentials[0][0],self.client_credentials[0][1]))
				 print("Döngü sonlandırılıyor ....")
				 self.create_recv_thread()
				 self.condition = False
			except Exception as conn_err:
				print("İstemci bağlanırken bir hata oluştu ",conn_err)
	def accept_connections(self):
		thread = threading.Thread(target = self.socket_loop)
		thread.daemon = True
		thread.start()
	def create_recv_thread(self):
		print("Veri alım işlemi başladı !!")
		def inner_recv_function(socket):
			while True:
				data = socket.recv(1024)
				if not data is None:
					if data == b"KILL_SESSION":
						print("Hoşçakal istemci o halde bende kendimi kapatıyorum !!!")
						socket.close()
						break
					print("Veri alındı! uzunluk %s \nVeri: %s" % (len(data),data.decode("utf-8")))
		thread = threading.Thread(target = inner_recv_function,args = (self.client_credentials[1],))
		thread.daemon = True
		thread.start()
	def send(self,data_to_send: bytes):
		try:
			self.client_credentials[1].send(data_to_send.encode())
			print("Veri gönderildi ! uzunluk:%s " % (len(data_to_send)))
		except Exception as send_error:
			print("Veri gönderilemedi !",send_error)
	def send_kill_message(self):
		self.send("KILL_SESSION")
class Console(cmd):
	def __init__(self):
		cmd.__init__(self)
		self.sock = BindSocket("127.0.0.1",4444)
		self.sock.init_sock()
	def do_send(self,data: bytes):
		self.sock.send(data)
	def do_exit(self,*args):
		self.sock.send_kill_message()
		return True # çıkmak için
if __name__ == "__main__":
	cmd = Console()
	cmd.prompt = "(Server)> "
	cmd.cmdloop()
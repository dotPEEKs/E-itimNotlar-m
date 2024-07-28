import threading
import socket
from cmd import Cmd as cmd
class Client:
	def __init__(self,ip,port):
		self.ip = ip
		self.port = port
		self.condition = True
	def init_sock(self):
		print("Bağlanılıyor ....")
		self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.counter = 1
		while True:
			try:
				self.socket.connect((self.ip,self.port))
				break 
			except:
				print("Deneme: %s lütfen sunucunun açık olduğundan emin olun !!!" % (self.counter))
				self.counter+=1
				"""
				Burada döngü sonlanmayacak çünkü server açık değil
				"""
		self.create_recv_thread()
	def create_recv_thread(self):
		print("Veri alım işlemi başladı !!")
		def inner_recv_function(socket):
			while True:
				data = socket.recv(1024)
				if not data is None:
					if data == b"KILL_SESSION":
						print("Tamamdır sunucu sen gittiğine göre bende soketi kapatıyorum !")
						socket.close()
						break
					print("Veri alındı! uzunluk %s \nVeri: %s" % (len(data),data.decode("utf-8")))
		thread = threading.Thread(target = inner_recv_function,args = (self.socket,))
		thread.daemon = True
		thread.start()
	def send(self,data_to_send: bytes):
		try:
			self.socket.send(data_to_send.encode())
			print("Veri gönderildi ! uzunluk:%s " % (len(data_to_send)))
		except Exception as send_error:
			print("Veri gönderilemedi !",send_error)
class Console(cmd):
	def __init__(self):
		cmd.__init__(self)
		self.sock = Client("127.0.0.1",4444)
		self.sock.init_sock()
	def do_send(self,data: bytes):
		self.sock.send(data)
	def do_exit(self,*args):
		self.sock.send("KILL_SESSION")
		return True # çıkmak için
if __name__ == "__main__":
	cmd = Console()
	cmd.prompt = "(Client)> "
	cmd.cmdloop()
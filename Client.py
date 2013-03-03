import socket
import World


class Client:
	"""Client."""

	def __init__(self, host, port):
		self.addr = (host, port)
		self.s = socket.socket()
		self.s.connect(self.addr)
	
	def __del__(self):
		self.s.close()

	def scan(self):
		running = true
		while running:
			try:
				data = self.s.recv(1024)
				items = data.split(",")
				if item[0] == "INIT":
					self.set_width_height(self, item[1], item[2])
					self.set_char(self, item[3])
					print "initialized!"
				else:
					print data
			except KeyboardInterrupt:
				running = false
		self.s.close()
		
	def send(self, message):
		self.s.send(message)
	
	def set_width_height(self, w, h):
		self.width = w
		self.height = h
	
	def get_width(self):
		return self.width
	
	def get_height(self):
		return self.height
	
	def set_char(self, char):
		self.char = char
	
	def get_char(self):
		return self.char

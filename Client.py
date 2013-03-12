import socket
import World


class Client:
	"""Client."""

	def __init__(self, host, port):
		self.addr = (host, port)
		self.s = socket.socket()
		self.s.connect(self.addr)
		self.s.settimeout(1.0)

	def __del__(self):
		self.s.close()

	def scan(self):
		running = True
		while running:
			try:
				try:
					data = self.s.recv(1024)
					if len(data) == 0:
						running = False
						print "Closed connection (server stop)."
						self.s.close()
						break
					messages = data.split(";")
					for message in messages:
						items = message.split(",")
						if len(message) == 0:
							continue
						elif items[0] == "INIT":
							self.init_world(int(items[1]), int(items[2]))
							self.set_char(items[3])
							print "Initialized! Char is `" + self.get_char() + "'."
						else:
							print "Message: " + message
				except socket.timeout:
					pass
			except KeyboardInterrupt:
				running = False
		del(self)

	def send(self, message):
		self.s.send(message)

	def init_world(self, width, height):
		self.world = World.World(width, height)

	def set_char(self, char):
		self.char = char

	def get_char(self):
		return self.char

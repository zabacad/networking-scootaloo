import socket
import World


class Client:
	"""Client."""

	def __init__(self, port, char, width, height):
		self.addr = ("localhost", port)
		self.s = socket.socket()
		self.s.connect(self.addr)
		self.world = World.World(width, height)

		self.char = char

	def __del__(self):
		self.s.close()

	def scan(self):
		pass

	def send(self, message):
		self.s.send(message)

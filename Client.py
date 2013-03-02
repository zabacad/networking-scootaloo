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

	def send_move(self, x, y):
		self.s.send(x + "," + y)
		
	def scan(self):
		while 1:
			self.s.send(input())

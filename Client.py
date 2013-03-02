import socket


class Client:
	"""Client."""

	def __init__(self, port, char):
		self.addr = ('', port)
		self.s = socket.socket()
		self.s.connect(self.addr)

		self.char = char

	def __del__(self):
		self.s.close()

	def send_move(self, x, y):
		self.s.send("Move")

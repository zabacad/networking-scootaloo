

class Client:
	"""Client."""

	def __init__(self, server, char):
		self.server = server
		self.char = char

	def __del__(self):
		pass
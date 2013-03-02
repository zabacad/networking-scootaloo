class World:
	"""World."""

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.world = [[" " for x in xrange(x)] for y in xrange(y)]

	def __del__(self):
		pass

	def get(self, x, y):
		return self.world[x][y]

	def set(self, x, y, char):
		self.world[x][y] = char

	def reset(self, x, y):
		self.set(x, y, " ")

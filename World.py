class World:
	"""World."""

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.world = [[" " for x in xrange(self.width)] for y in xrange(self.height)]

	def __del__(self):
		pass

	def __str__(self):
		printable = ""
		for y in xrange(self.height):
			for x in xrange(self.width):
				printable += str(self.get(x, y))
			printable += "\n"
		return printable

	def get(self, x, y):
		return self.world[y][x]

	def set(self, x, y, char):
		self.world[y][x] = char

	def reset(self, x, y):
		self.set(x, y, " ")

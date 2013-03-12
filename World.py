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

	def get_list(self):
		return [item for sublist in self.world for item in sublist]

	def set(self, x, y, char):
		self.world[y][x] = char

	def reset(self, x, y):
		self.set(x, y, " ")

	def get_width_height(self):
		return (self.width, self.height)

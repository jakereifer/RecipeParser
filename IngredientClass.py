class Ingredient(object):
	name = ""
	quantity = 0
	measurement = ""
	descriptor = ""
	preparation = ""
	tags = []

	def __init__(self, name="", quantity=0, measurement="", desc="", prep="", tags=[]):
		self.name = name
		self.quantity = quantity,
		self.measurement = measurement
		self.descriptor = desc
		self.preparation = prep
		self.tags = tags

	# Print the ingredient in a human friendly manner
	def printIngredient(self):
		if self.name:
			print("Name: ", self.name)
		if self.quantity:
			print("Quantity: ", self.quantity)
		if self.measurement:
			print("Measurement: ", self.measurement)
		if self.descriptor:
			print("Descriptor: ", self.descriptor)
		if self.preparation:
			print("Preparation: ", self.preparation)
		if self.tags:
			print("Tags: ", self.tags)
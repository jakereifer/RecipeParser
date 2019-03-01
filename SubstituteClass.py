from IngredientClass import *
from RecipeClass import *

class Substitute(object):
	name = ""
	methods = {}
	quantity = {}
	tools = {}
	
	def __init__(self, name="", methods={}, quantity={}, tools{}):
		self.name = name
		self.methods = methods
		self.quantity = quantity
		self.tools = tools
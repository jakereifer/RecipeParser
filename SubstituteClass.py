from IngredientClass import *
from RecipeClass import *

class Substitute(object):
	canreplace = []
	methods = {}
	quantity = {}
	tools = {}
	
	
	def __init__(self, canreplace=[], methods={}, quantity={}, tools={}):
		self.canreplace = canreplace
		self.methods = methods
		self.quantity = quantity
		self.tools = tools
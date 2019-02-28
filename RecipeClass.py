import knowledgebase
from helpers import *
from IngredientClass import *
from StepClass import *
from ingredientparser import *

class Recipe(object):
	name = ""
	ingredients = []
	steps = []
	p_methods = []
	s_methods = []
	tools = []
	categories = { "healthy": [],
					"unhealthy": [],
					"vegetarian": [],
					"not vegetarian": []}

	def __init__(self, name="", ingredients=[], steps=[], p_methods=[], s_methods=[], tools=[], categories={ "healthy": [],"unhealthy": [], "vegetarian": [], "not vegetarian": []}):
		self.name = name
		self.ingredients = ingredients
		self.steps = steps
		self.p_methods = p_methods
		self.s_methods = s_methods
		self.tools = tools
		self.categories = categories

	def sortIngredientsIntoCategories(self):
		for category in self.categories.keys():
			for ingredient in self.ingredients:
				if category in ingredient.tags:
					self.categories[category].append(ingredient)

	def printRecipe(self):
		if self.name:
			print("Name: ", self.name)
		if self.ingredients:
			print("\nINGREDIENTS:")
			for i in self.ingredients:
				i.printIngredient()
		if self.steps:
			print("\nSTEPS:")
			for s in self.steps:
				s.printStep()
		if self.p_methods:
			print("\nPRIMARY METHODS: ", self.p_methods)
		if self.s_methods:
			print("\nSECONDARY METHODS: ", self.s_methods)
		if self.tools:
			print("\nTOOLS: ", self.tools)
		if self.categories:
			print("\nSORTED INGREDIENTS:")
			for cat in self.categories.keys():
				print(cat.title() + ": ", [i.name for i in self.categories[cat]])
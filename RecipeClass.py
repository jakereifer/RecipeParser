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
			print("Name: ", i.name)
		if self.ingredients:
			print("INGREDIENTS:")
			for i in self.ingredients:
				i.printIngredient()
		if self.steps:
			print("STEPS:")
			for s in self.steps:
				printStepInfo(s)
		if self.p_methods:
			print("PRIMARY METHODS: ", self.p_methods)
		if self.s_methods:
			print("SECONDARY METHODS: ", self.s_methods)
		if self.tools:
			print("TOOLS: ", self.tools)
		if self.categories:
			print("SORTED INGREDIENTS:")
			for cat in self.categories.keys():
				print(cat.title() + ": ", [i.name for i in categories[cat]])
# returns a list of the "keywords" found in "strings"
import ingredientparser
def findWordsInSteps(keywords, strings):
	keywordsfound = []
	for string in strings:
		for keyword in keywords:
			if keyword in string.lower():
				keywordsfound.append(keyword.capitalize())
	return keywordsfound


class Recipe(object):
	name = ""
	ingredients = []
	steps = []
	p_methods = []
	s_methods = []
	tools = []
	tags = []


	def __init__(self, name="", ingredients=[], steps=[], p_methods=[], s_methods=[], tools=[], tags=[]):
		self.name = name
		self.ingredients = ingredients
		self.steps = steps
		self.p_methods = p_methods
		self.s_methods = s_methods
		self.tools = tools
		self.tags = tags

	def display(self):
		print("Recipe Name: ", self.name)
		print("Tools Needed: ", self.tools)
		print("Primary Methods Used: ", self.p_methods)
		print("Secondary Methods Used: ", self.s_methods)
		print("List of Ingredients:")
		for i in self.ingredients:
			ingredientparser.printIngredient(i)
		print("\n")
		print("List of Steps:")
		for s in self.steps:
			print(s)
		print("\n")

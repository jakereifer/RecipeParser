# returns a list of the "keywords" found in "strings"
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
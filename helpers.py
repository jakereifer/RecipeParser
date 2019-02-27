import validators

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


class Ingredient(object):
	name = ""
	quantity = 0
	measurement = ""
	descriptor = ""
	preparation = ""
	category = ""
	subcategory = ""

	def __init__(self, name="", quantity=0, measurement="", desc="", prep="", category="", subcategory=""):
		self.name = name
		self.quantity = quantity,
		self.measurement = measurement
		self.descriptor = desc
		self.preparation = prep
		self.category = category
		self.subcategory = subcategory


transformations = { 0: "NONE",
					1: "TO_VEGETARIAN",
					2: "FROM_VEGETARIAN",
					3: "TO_HEALTHY",
					4: "FROM_HEALTHY", 
					5: "TO_CUISINE",
					6: "FROM_CUISINE" }

def validatePageLink(err=False):
	if err:
		print("** INVALID URL **\n Please try again.")
	inp = input("Please enter a recipe URL: ")
	page_link = inp if validators.url(inp) else (validatePageLink(True))
	return page_link

def validateTransform(err=False):
	if err:
		print("** INVALID TRANSFORM **\n Please try again.")

	print("\nRecipe Transformations:")
	for k, v in transformations.items():
	     print("%d\t%s" % (k, v))
	inp = input("Please enter the number corresponding to the transformation you'd like to perform:\t")
	transf = int(inp) if int(inp) in transformations.keys() else (validateTransform(True))
	return transf
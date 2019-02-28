import pandas as pd
from pprint import pprint 
# import measurements
from helpers import Ingredient

class Unit(object):
	name = ''
	aliases = []

	def __init__(self, n='', a=[]):
		self.name = n
		self.aliases = a

measurements = {'volume': [ Unit('teaspoon', ['t', 'tsp']),
							Unit('tablespoon', ['T', 'tbl', 'tbs', 'tbsp']),
							Unit('fluid ounce',['fl oz']),
							Unit('cup', ['c']),
							Unit('pint', ['p', 'pt', 'fl pt']),
							Unit('quart', ['q', 'qt', 'fl qt']),
							Unit('gallon', ['g', 'gal']),
							Unit('milliliter', ['ml', 'millilitre', 'mL']),
							Unit('liter', ['l', 'L', 'litre'])],
				'mass/weight': [ Unit('pound',  ['lb', '#']),
								Unit('ounce', ['oz']),
								Unit('milligram', ['mg', 'milligramme']),
								Unit('gram', ['g', 'gramme']),
								Unit('kilogram', ['kg', 'kilogramme'])],
				'time': [ Unit('day',[]),
						Unit('hour', ['hr']),
						Unit('minute', ['min']),
						Unit('second', ['sec', 's'])]
				}

# not case sensitiv
#veg_proteins
# veg_proteins = [ Ingredient(name="tofu", category="protein", subcategory="veg_protein"), Ingredient(name="tempeh", category="protein", subcategory="veg_protein"), Ingredient(name="seitan", category="protein", subcategory="veg_protein"), Ingredient(name="jackfruit", category="protein", subcategory="veg_protein"), Ingredient(name="lentils", category="protein", subcategory="veg_protein"), Ingredient(name="beans", category="protein", subcategory="veg_protein"),
# 				Ingredient(name="legumes", category="protein", subcategory="veg_protein"), Ingredient(name="texturized vegetable protein (TVP)", category="protein", subcategory="veg_protein"),#tvp
# 				Ingredient(name="chickpeas", category="protein", subcategory="veg_protein"), Ingredient(name="falafel", category="protein", subcategory="veg_protein"), Ingredient(name="nuts", category="protein", subcategory="veg_protein"), Ingredient(name="soy", category="protein", subcategory="veg_protein"), Ingredient(name="vegetarian bacon", category="protein", subcategory="veg_protein"), Ingredient(name="veggie burger", category="protein", subcategory="veg_protein"),
# 				Ingredient(name="tofurkey", category="protein", subcategory="veg_protein"), Ingredient(name="veggie dog", category="protein", subcategory="veg_protein"), Ingredient(name="quinoa", category="protein", subcategory="veg_protein"), Ingredient(name='chik\'n', category="protein", subcategory="veg_protein")]

# meat_subs = { Ingredient(name='hamburger', category="protein", subcategory="meat"): [Ingredient(name='veggie burger', category="protein", subcategory="veg_protein"), Ingredient(name='black bean burger', category="protein", subcategory="veg_protein")],
# 				Ingredient(name='meatball', category="protein", subcategory="meat"): [Ingredient(name='veggie meatballs', category="protein", subcategory="veg_protein")],
# 				Ingredient(name='hot dog', category="protein", subcategory="meat"): [Ingredient(name='veggie dog', category="protein", subcategory="veg_protein")],
# 				Ingredient(name='sausage', category="protein", subcategory="meat"): [Ingredient(name='veggie sausage', category="protein", subcategory="veg_protein"), Ingredient(name='tempeh', category="protein", subcategory="veg_protein")],
# 				Ingredient(name='chicken', category="protein", subcategory="meat"): [Ingredient(name='chik\'n', category="protein", subcategory="veg_protein"), Ingredient(name='tofu', category="protein", subcategory="veg_protein"), Ingredient(name='seitan', category="protein", subcategory="veg_protein")],
# 				Ingredient(name='default', category="protein", subcategory="meat"): [Ingredient(name='tofu', category="protein", subcategory="veg_protein"), Ingredient(name="texturized vegetable protein (TVP)", category="protein", subcategory="veg_protein")],
# 				Ingredient(name='pork', category="protein", subcategory="meat"): [Ingredient(name='seitan', category="protein", subcategory="veg_protein")],
# 				Ingredient(name='turkey', category="protein", subcategory="meat"): [Ingredient(name='tofurkey', category="protein", subcategory="veg_protein")],
# 				Ingredient(name='beef', category="protein", subcategory="meat"): [Ingredient(name='tofu', category="protein", subcategory="veg_protein"), Ingredient(name='seitan', category="protein", subcategory="veg_protein")],
# 				Ingredient(name='fish', category="protein", subcategory="meat"): [Ingredient(name='tofu', category="protein", subcategory="veg_protein")],
# 				Ingredient(name='chorizo', category="protein", subcategory="meat"): [Ingredient(name='beans', category="protein", subcategory="veg_protein")]
# 			}

ingredients_kb = [
	Ingredient(name="abalone", tags=["not vegetarian", "healthy"]),
	Ingredient(name="achovy", tags=["not vegetarian", "healthy"]),
	Ingredient(name="arctic char", tags=["not vegetarian", "healthy"]),
	Ingredient(name="bacon", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="beef", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="bison", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="blood", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="burger", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="calamari", tags=["not vegetarian", "healthy"]),
	Ingredient(name="catfish", tags=["not vegetarian", "healthy"]),
	Ingredient(name="caviar", tags=["not vegetarian", "healthy"]),
	Ingredient(name="chicken", tags=["not vegetarian", "healthy"]),
	Ingredient(name="chorizo", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="clam", tags=["not vegetarian", "healthy"]),
	Ingredient(name="cockle", tags=["not vegetarian", "healthy"]),
	Ingredient(name="cod", tags=["not vegetarian", "healthy"]),
	Ingredient(name="conch", tags=["not vegetarian", "healthy"]),
	Ingredient(name="cornish game hen", tags=["not vegetarian", "healthy"]),
	Ingredient(name="crab", tags=["not vegetarian", "healthy"]),
	Ingredient(name="crayfish", tags=["not vegetarian", "healthy"]),
	Ingredient(name="duck", tags=["not vegetarian", "healthy"]),
	Ingredient(name="fish", tags=["not vegetarian", "healthy"]),
	Ingredient(name="foie gras", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="game", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="giblets", tags=["not vegetarian", "healthy"]),
	Ingredient(name="goat", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="goose", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="guinea pig", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="hagfish", tags=["not vegetarian", "healthy"]),
	Ingredient(name="halibut", tags=["not vegetarian", "healthy"]),
	Ingredient(name="ham", tags=["not vegetarian", "healthy"]),
	Ingredient(name="hedgehog", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="horse", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="hot dog", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="ikura", tags=["not vegetarian", "healthy"]),
	Ingredient(name="kidney", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="kielbasa", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="lamb", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="liver", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="lobster", tags=["not vegetarian", "healthy"]),
	Ingredient(name="mahi mahi", tags=["not vegetarian", "healthy"]),
	Ingredient(name="meatballs", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="molluscs oyster", tags=["not vegetarian", "healthy"]),
	Ingredient(name="mortadella", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="mussel", tags=["not vegetarian", "healthy"]),
	Ingredient(name="mutton", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="neck sweetbread", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="octopus", tags=["not vegetarian", "healthy"]),
	Ingredient(name="organ meat", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="ostrich", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="pancetta", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="pastrami", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="pepperoni", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="pipi", tags=["not vegetarian", "healthy"]),
	Ingredient(name="pork", tags=["not vegetarian", "healthy"]),
	Ingredient(name="proscuitto", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="quail", tags=["not vegetarian", "healthy"]),
	Ingredient(name="rabbit", tags=["not vegetarian", "healthy"]),
	Ingredient(name="salami", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="salmon", tags=["not vegetarian", "healthy"]),
	Ingredient(name="sardine", tags=["not vegetarian", "healthy"]),
	Ingredient(name="sausage", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="sausage casing", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="scallop", tags=["not vegetarian", "healthy"]),
	Ingredient(name="sea cucumber", tags=["not vegetarian", "healthy"]),
	Ingredient(name="shark", tags=["not vegetarian", "healthy"]),
	Ingredient(name="shrimp", tags=["not vegetarian", "healthy"]),
	Ingredient(name="snail", tags=["not vegetarian", "healthy"]),
	Ingredient(name="squid", tags=["not vegetarian", "healthy"]),
	Ingredient(name="squirrel", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="steak", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="stomach sweetbread", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="sturgeon", tags=["not vegetarian", "healthy"]),
	Ingredient(name="sweetbread", tags=["not vegetarian", "healthy"]),
	Ingredient(name="swordfish", tags=["not vegetarian", "healthy"]),
	Ingredient(name="tongue", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="tripe", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="trout", tags=["not vegetarian", "healthy"]),
	Ingredient(name="tuna", tags=["not vegetarian", "healthy"]),
	Ingredient(name="turkey", tags=["not vegetarian", "healthy"]),
	Ingredient(name="uni", tags=["not vegetarian", "healthy"]),
	Ingredient(name="veal", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="venison", tags=["not vegetarian", "unhealthy"]),
	Ingredient(name="whelk", tags=["not vegetarian", "healthy"]),
	Ingredient(name="winkle", tags=["not vegetarian", "healthy"]),
	Ingredient(name="white bread", tags=["unhealthy", "unhealthy"]),
	Ingredient(name="beans", tags=["vegetarian", "healthy"]),
	Ingredient(name="chickpeas", tags=["vegetarian", "healthy"]),
	Ingredient(name="chik'n", tags=["vegetarian", "healthy"]),
	Ingredient(name="condensed milk", tags=["unhealthy"]),
	Ingredient(name="cream", tags=["unhealthy"]),
	Ingredient(name="egg", tags=["vegetarian", "healthy"]),
	Ingredient(name="egg white", tags=["vegetarian", "healthy"]),
	Ingredient(name="egg yolk", tags=["vegetarian", "unhealthy"]),
	Ingredient(name="falafel", tags=["vegetarian", "healthy"]),
	Ingredient(name="ghee", tags=["healthy"]),
	Ingredient(name="jackfruit", tags=["vegetarian", "healthy"]),
	Ingredient(name="kefir", tags=["healthy"]),
	Ingredient(name="lassi", tags=["vegetarian", "healthy"]),
	Ingredient(name="legumes", tags=["vegetarian", "healthy"]),
	Ingredient(name="lentils", tags=["vegetarian", "healthy"]),
	Ingredient(name="milk", tags=["healthy"]),
	Ingredient(name="pasta", tags=["unhealthy"]),
	Ingredient(name="quinoa", tags=["healthy"]),
	Ingredient(name="seitan", tags=["vegetarian", "healthy"]),
	Ingredient(name="sour cream", tags=["healthy"]),
	Ingredient(name="tempeh", tags=["vegetarian", "healthy"]),
	Ingredient(name="texturized vegetable protein (tvp)", tags=["vegetarian", "healthy"]),
	Ingredient(name="tofu", tags=["vegetarian", "healthy"]),
	Ingredient(name="tofurkey", tags=["vegetarian", "healthy"]),
	Ingredient(name="vegetarian bacon", tags=["vegetarian", "healthy"]),
	Ingredient(name="veggie burger", tags=["vegetarian", "healthy"]),
	Ingredient(name="veggie dog", tags=["vegetarian", "healthy"]),
	Ingredient(name="whipped cream", tags=["unhealthy"]),
	Ingredient(name="white rice", tags=["unhealthy"]),
	Ingredient(name="whole wheat flour", tags=["healthy"]),
	Ingredient(name="yogurt", tags=["healthy"]),
	Ingredient(name="tortilla", tags=["unhealthy"]),
	Ingredient(name="flour tortilla", tags=["unhealthy"]),
	Ingredient(name="corn tortilla", tags=["healthy"]),
	Ingredient(name="sugar", tags=["unhealthy"]),
	Ingredient(name="stevia", tags=["healthy"]),
	Ingredient(name="chocolate chips", tags=["unhealthy"]),
	Ingredient(name="cacao nibs ", tags=["healthy"]),
	Ingredient(name="almond milk", tags=["healthy"]),
	Ingredient(name="coconut milk", tags=["healthy"]),
	Ingredient(name="all-purpouse flour", tags=["unhealthy"]),
	Ingredient(name="bohrani", tags=["healthy"]),
	Ingredient(name="brown rice", tags=["healthy"]),
	Ingredient(name="butter", tags=["unhealthy"]),
	Ingredient(name="buttermilk", tags=["unhealthy"]),
	Ingredient(name="cheese", tags=["unhealthy"])
]

cs = ["healthy", "unhealthy", "vegetarian", "not vegetarian"]
categories = {}

for c in cs:
	categories[c] = []

for ingr in ingredients_kb:
	for c in cs:
		if c in ingr.tags:
			categories[c].append(ingr)





# REGEX: get before new line (.*)(\n)
# replace: Ingredient(name="\1", category="healthy", subcategory="vegetable"),\2


tools = ["baking sheet","blender","bowl","box grater","brush","can opener","cast iron skillet",
		"colander","cutting board","double boiler","dutch oven","foil","food processer ","fork","frying pan",
		"funnel","garlic press","grill","hand mixer","knife","ladel","mandoline","measuring cup","microplane", 
		"mortar","paper towel","parchment paper","paring knife","peeler","pesltle","plastic wrap","plate","pot",
		"rack",'ramekin',"roasting pan","rolling pin","saucepan","sheet pan","sieve","skewer","skillet","smoker",
		"spatula","spoon","stand mixer","stock pot","thermometer","timer","tongs","twine","whisk", "sifter", "strainer", "mallet"]

primary_methods = ["bake","barbeque","boil","broil","braise","carmelize","flambe","fry","grill",
					"parbake","parboil","poach","roast","sear", "smoke","steam","saute", "sauté" "simmer",
					"stir fry","stew","sweat","toast", "baste", "melt", "reduce", "render", "temper", "freeze", "clarify"]

secondary_methods = ["arange","add","heat","brown","beat","blache","heat","cover","chop","combine",
					"crush","cube","cut","deglaze","dice","form", "fold","grind","julienne" ,"knead","mince","mix",
					"pound","preheat","pour","roll","rub","season","shredd","skewer","slice","stir","transfer","tenderize","whisk",
					"spoon", "drain", "sprinkle", "top", "layer", "lay", "place", "set", "strain", "line", "oil", "butter", "prepare",
					"refrigerate", "arrange", "turn", "flip", "brush", "galze", "dip" , "spread", "press", "coat", "pat", "save", "reserve", 
					"put", "return", "scrape", "peel", "rinsed", "remove", "repeat", "allow", "rest", "toss", "distribute", "wash", "fill",
					"mash", "smash", "blend", "cool", "store", "cream", "drop", "dissolve"]

units = ["bag","teaspoon","tablespoon","ounce","clove","cup","pint","quart","gallon",
		"milliliter","liter","pound","gram","milligram","kilogram","pinch", "pinches", "handful","head",
		"loaf","loaves","can","package", "pack","bunch","bushel","T","tsp",'t',"tbl","tbsp",'tbs','c','p','gal','g']

preparations = ["chopped","shredded","ground","crushed","sliced","cooked","pureed",
				"peeled","smoked","minced","rinsed","trimmed","uncooked","rolled","pounded","cut","diced", "halved", "melted", "frozen", "clarified"]

"""
method_tools = {
	"bake" : "oven",
	"barbeque": "barbeque",
	"boil": "pot",
	"broil": "oven",
	"braise": "pot",
	"carmelize" : "pan",
	"flambe": "man",
	"fry": "pan",
	"parkbake": "oven",
	"parboil": "pot",
	"poach": "pot",
	"roast": "oven",
	"sear": "pan",
	"smoke": "smoker",
	"steam": "pot",
	"saute": "pan",
	"sauté" : "pan",
	"simmer": "pot",
	"stir fry": "pan",
	"stew": "pot",
	"sweat": "pan",
	"toast": "toaster",

}
"""
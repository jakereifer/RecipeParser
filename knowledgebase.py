import pandas as pd
from pprint import pprint
from IngredientClass import *
from SubstituteClass import *

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
	Ingredient(name="abalone", tags=[1, 3]),
	Ingredient(name="achovy", tags=[1, 3]),
	Ingredient(name="arctic char", tags=[1, 3]),
	Ingredient(name="bacon", tags=[1, 4]),
	Ingredient(name="beef", tags=[1, 4]),
	Ingredient(name="bison", tags=[1, 4]),
	Ingredient(name="blood", tags=[1, 4]),
	Ingredient(name="burger", tags=[1, 4]),
	Ingredient(name="calamari", tags=[1, 3]),
	Ingredient(name="catfish", tags=[1, 3]),
	Ingredient(name="caviar", tags=[1, 3]),
	Ingredient(name="chicken", tags=[1, 3]),
	Ingredient(name="chorizo", tags=[1, 4]),
	Ingredient(name="clam", tags=[1, 3]),
	Ingredient(name="cockle", tags=[1, 3]),
	Ingredient(name="cod", tags=[1, 3]),
	Ingredient(name="conch", tags=[1, 3]),
	Ingredient(name="cornish game hen", tags=[1, 3]),
	Ingredient(name="crab", tags=[1, 3]),
	Ingredient(name="crayfish", tags=[1, 3]),
	Ingredient(name="duck", tags=[1, 3]),
	Ingredient(name="fish", tags=[1, 3]),
	Ingredient(name="foie gras", tags=[1, 4]),
	Ingredient(name="game", tags=[1, 4]),
	Ingredient(name="giblets", tags=[1, 3]),
	Ingredient(name="goat", tags=[1, 4]),
	Ingredient(name="goose", tags=[1, 4]),
	Ingredient(name="guinea pig", tags=[1, 4]),
	Ingredient(name="hagfish", tags=[1, 3]),
	Ingredient(name="halibut", tags=[1, 3]),
	Ingredient(name="ham", tags=[1, 3]),
	Ingredient(name="hedgehog", tags=[1, 4]),
	Ingredient(name="horse", tags=[1, 4]),
	Ingredient(name="hot dog", tags=[1, 4]),
	Ingredient(name="ikura", tags=[1, 3]),
	Ingredient(name="kidney", tags=[1, 4]),
	Ingredient(name="kielbasa", tags=[1, 4]),
	Ingredient(name="lamb", tags=[1, 4]),
	Ingredient(name="liver", tags=[1, 4]),
	Ingredient(name="lobster", tags=[1, 3]),
	Ingredient(name="mahi mahi", tags=[1, 3]),
	Ingredient(name="meatballs", tags=[1, 4]),
	Ingredient(name="molluscs oyster", tags=[1, 3]),
	Ingredient(name="mortadella", tags=[1, 4]),
	Ingredient(name="mussel", tags=[1, 3]),
	Ingredient(name="mutton", tags=[1, 4]),
	Ingredient(name="neck sweetbread", tags=[1, 4]),
	Ingredient(name="octopus", tags=[1, 3]),
	Ingredient(name="organ meat", tags=[1, 4]),
	Ingredient(name="ostrich", tags=[1, 4]),
	Ingredient(name="pancetta", tags=[1, 4]),
	Ingredient(name="pastrami", tags=[1, 4]),
	Ingredient(name="pepperoni", tags=[1, 4]),
	Ingredient(name="pipi", tags=[1, 3]),
	Ingredient(name="pork", tags=[1, 3]),
	Ingredient(name="proscuitto", tags=[1, 4]),
	Ingredient(name="quail", tags=[1, 3]),
	Ingredient(name="rabbit", tags=[1, 3]),
	Ingredient(name="salami", tags=[1, 4]),
	Ingredient(name="salmon", tags=[1, 3]),
	Ingredient(name="sardine", tags=[1, 3]),
	Ingredient(name="sausage", tags=[1, 4]),
	Ingredient(name="sausage casing", tags=[1, 4]),
	Ingredient(name="scallop", tags=[1, 3]),
	Ingredient(name="sea cucumber", tags=[1, 3]),
	Ingredient(name="shark", tags=[1, 3]),
	Ingredient(name="shrimp", tags=[1, 3]),
	Ingredient(name="snail", tags=[1, 3]),
	Ingredient(name="squid", tags=[1, 3]),
	Ingredient(name="squirrel", tags=[1, 4]),
	Ingredient(name="steak", tags=[1, 4]),
	Ingredient(name="stomach sweetbread", tags=[1, 4]),
	Ingredient(name="sturgeon", tags=[1, 3]),
	Ingredient(name="sweetbread", tags=[1, 3]),
	Ingredient(name="swordfish", tags=[1, 3]),
	Ingredient(name="tongue", tags=[1, 4]),
	Ingredient(name="tripe", tags=[1, 4]),
	Ingredient(name="trout", tags=[1, 3]),
	Ingredient(name="tuna", tags=[1, 3]),
	Ingredient(name="turkey", tags=[1, 3]),
	Ingredient(name="uni", tags=[1, 3]),
	Ingredient(name="veal", tags=[1, 4]),
	Ingredient(name="venison", tags=[1, 4]),
	Ingredient(name="whelk", tags=[1, 3]),
	Ingredient(name="winkle", tags=[1, 3]),
	Ingredient(name="white bread", tags=[4, 4]),
	Ingredient(name="beans", tags=[2, 3]),
	Ingredient(name="chickpeas", tags=[2, 3]),
	Ingredient(name="chik'n", tags=[2, 3]),
	Ingredient(name="condensed milk", tags=[4]),
	Ingredient(name="cream", tags=[4]),
	Ingredient(name="egg", tags=[2, 3]),
	Ingredient(name="egg white", tags=[2, 3]),
	Ingredient(name="egg yolk", tags=[2, 4]),
	Ingredient(name="falafel", tags=[2, 3]),
	Ingredient(name="ghee", tags=[3]),
	Ingredient(name="jackfruit", tags=[2, 3]),
	Ingredient(name="kefir", tags=[3]),
	Ingredient(name="lassi", tags=[2, 3]),
	Ingredient(name="legumes", tags=[2, 3]),
	Ingredient(name="lentils", tags=[2, 3]),
	Ingredient(name="milk", tags=[3]),
	Ingredient(name="pasta", tags=[4]),
	Ingredient(name="quinoa", tags=[3]),
	Ingredient(name="seitan", tags=[2, 3]),
	Ingredient(name="sour cream", tags=[3]),
	Ingredient(name="tempeh", tags=[2, 3]),
	Ingredient(name="texturized vegetable protein (tvp)", tags=[2, 3]),
	Ingredient(name="tofu", tags=[2, 3]),
	Ingredient(name="tofurky", tags=[2, 3]),
	Ingredient(name="veggie bacon strips", tags=[2, 3]),
	Ingredient(name="veggie burger", tags=[2, 3]),
	Ingredient(name="veggie dog", tags=[2, 3]),
	Ingredient(name="whipped cream", tags=[4]),
	Ingredient(name="white rice", tags=[4]),
	Ingredient(name="whole wheat flour", tags=[3]),
	Ingredient(name="yogurt", tags=[3]),
	Ingredient(name="tortilla", tags=[4]),
	Ingredient(name="flour tortilla", tags=[4]),
	Ingredient(name="corn tortilla", tags=[3]),
	Ingredient(name="sugar", tags=[4]),
	Ingredient(name="stevia", tags=[3]),
	Ingredient(name="chocolate chips", tags=[4]),
	Ingredient(name="cacao nibs ", tags=[3]),
	Ingredient(name="almond milk", tags=[3]),
	Ingredient(name="coconut milk", tags=[3]),
	Ingredient(name="all-purpose flour", tags=[4]),
	Ingredient(name="bohrani", tags=[3]),
	Ingredient(name="brown rice", tags=[3]),
	Ingredient(name="butter", tags=[4]),
	Ingredient(name="buttermilk", tags=[4]),
	Ingredient(name="cheese", tags=[4,5]),
	Ingredient(name="turmeric", tags=["seasoning"]),
	Ingredient(name="basil", tags=["seasoning"]),
	Ingredient(name="ginger", tags=["seasoning"]),
	Ingredient(name="nutmeg", tags=["seasoning"]),
	Ingredient(name="cinnamon", tags=["seasoning"]),
	Ingredient(name="curry powder", tags=["seasoning"]),
	Ingredient(name="cayenne pepper", tags=["seasoning"]),
	Ingredient(name= "thyme", tags=["seasoning"]),
	Ingredient(name= "garam masala", tags=["seasoning"]),
	Ingredient(name= "rosemary", tags=["seasoning"]),
	Ingredient(name= "sage", tags=["seasoning"]),
	Ingredient(name= "parsley", tags=["seasoning"]),
	Ingredient(name= "italian seasoning", tags=["seasoning"]),
]

substitute_map= {
1:{"tofu": Substitute(["shrimp", "pork", "chicken"],{},{"default":(.75,"cups") },{}), #non-vegetarian to vegetarian
	"seitan": Substitute(["beef", "salmon", "lamb"], {},{},{})},
2:{"ground beef": Substitute(["tofu", "seitan"],{},{},{})}, #from vegetarian to non-vegetarian
3:{"ground beef": Substitute(["tofu", "seitan"],{},{},{})},#from vegetarian to non-vegetarian
4:{"ground beef": Substitute(["tofu", "seitan"],{},{},{})}, #from vegetarian to non-vegetarian
5: {"jalapeno": Substitute(["green pepper", "bell pepper", "yellow pepper"],{},{"default":(5,"count") },{}),
	"lime juice": Substitute(["lemon juice", "lemon zest"],{},{"default":(1,"teaspoon")},{}), 
	"salsa": Substitute(["barbeque sauce", "marinara sauce", "pesto"],{},{"default":(.5,"cup")},{}),
	"cotija cheese": Substitute(["cheese"],{},{"default":(.25, "cup")},{})},
"seasoning": {} #to mexican
}

"""transformations_display = { 0: "None",
					1: "To vegetarian", # not vegetarian
					2: "From vegetarian", # vegetarian
					3: "From healthy", # healthy
					4: "To healthy", # unhealthy
					5: "To cuisine",
					6: "From cuisine" }"""
cs = [3, 4, 2, 1, "seasoning",5]
categories = {}

for c in cs:
	categories[c] = []

for ingr in ingredients_kb:
	for c in cs:
		if c in ingr.tags:
			categories[c].append(ingr)







# REGEX: get before new line (.*)(\n)
# replace: Ingredient(name="\1", category=3, subcategory="vegetable"),\2

tools = ["refrigerator","container", "baking sheet","blender","bowl","box grater","brush","can opener","cast iron skillet","colander","cutting board","double boiler", "oven", "foil","food processer ","fork","frying pan","funnel","garlic press","grill","hand mixer","knife","ladel","mandoline","measuring cup","microplane","mortar","paper towel","parchment paper","paring knife","peeler","pesltle","plastic wrap","plate","pot","rack",'ramekin',"roasting pan","rolling pin","saucepan","sheet pan","sieve","skewer","skillet","smoker","spatula","spoon","stand mixer","stock pot","thermometer","timer","tongs","twine","whisk", "sifter", "strainer", "mallet"]

primary_methods = ["cook","bake","serve","barbeque","boil","broil","braise","carmelize","flambe","fry","grill","parbake","parboil","poach","roast","sear", "smoke","steam","saute", "sauté" "simmer","stir fry","stew","sweat","toast", "baste", "melt", "reduce", "render", "temper", "freeze", "clarify", "spray"]

secondary_methods = ["refrigerate","remove", "lift", "arange","add","heat","brown","beat","blache","cover","chop","combine", "chill", "crush","cube","cut","deglaze","dice","form", "fold","grind","julienne" ,"knead","mince","mix","pound","preheat","pour","roll","rub","season","shredd","skewer","slice","stir","transfer","tenderize","whisk","spoon", "drain", "sprinkle", "top", "layer", "lay", "place", "set", "strain", "line", "prepare", "refrigerate", "arrange", "turn", "flip", "brush", "galze", "dip" , "spread", "press", "coat", "pat", "save", "reserve","put", "return", "scrape", "peel", "rinsed" "remove", "repeat", "allow","rest", "toss", "distribute", "wash", "fill","mash", "smash", "blend", "cool", "store", "cream", "drop", "dissolve"]

units = ["sprig","sprigs","bag","teaspoon","tablespoon","ounce","clove","cup","pint","quart","gallon", "milliliter","liter","pound","gram","milligram","kilogram","pinch", "pinches", "handful","head","loaf","loaves","can","package", "pack","bunch","bushel","T","tsp",'t',"tbl","tbsp",'tbs','c','p','gal','g']

preparations = ["chopped","shredded","ground","crushed","sliced","cooked","pureed","peeled","smoked","minced","rinsed","trimmed","uncooked","rolled","pounded","cut","diced", "halved", "melted", "frozen", "clarified"]

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
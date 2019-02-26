import pandas as pd
# import measurements

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

# not case sensitive
meats = ["Bacon", "Beef", "Bison", "Blood", "Chicken",
		 "Cooking Chicken","Chorizo", "Cornish Game Hen",
		 "Duck", "Foie Gras", "Game", "Giblets", "Goat",
		 "Goose", "Guinea Pig", "Ham", "Hedgehog", "Horse",
		 "Hot Dog", "Kidney", "Kielbasa", "Lamb", "Liver",
		 "Mortadella", "Mutton", "Neck Sweetbread", "Organ Meat",
		 "Ostrich", "Pancetta", "Pastrami", "Pepperoni", "Pork",
		 "Prosciutto", "Quail", "Rabbit", "Salami", "Sausage",
		 "Sausage Casing", "Squirrel", "Stomach Sweetbread",
		 "Sweetbread", "Tongue", "Tripe", "Turkey", "Veal", "Venison", "Burger", "Meatballs"]

# not case sensitive
seafood= ["Salmon", "Cod", "Halibut", "Mahi mahi", "Tuna", "Shark",
			"Swordfish", "Sturgeon", "Catfish", "Trout", "Sardine", 
			"Anchovy", "Arctic char", "Crab", "Crayfish", "Lobster", 
			"Shrimp", "Molluscs", "Abalone", "Clam", "Cockle", "Mussel",
			"Octopus", "Oyster", "Pipi", "Snail", "Conch", "Whelk",
			"Winkle", "Squid", "Calamari", "Scallop", "Caviar", "Uni",
			"Sea Cucumber", "Hagfish", "Tuna", "Ikura"]

#veg_proteins
veg_proteins = ['tofu', 'tempeh', 'seitan', 'jackfruit', 'lentils', 'beans',
				'legumes', 'texturized vegetable protein',#tvp
				'chickpeas', 'falafel', 'nuts', 'soy', 'vegetarian bacon', 'veggie burger'
				'tofurkey', 'vegetarian hot dog', 'quinoa']

meat_subs = {'burger': ['veggie burger', 'black bean burger'],
			'meatball': [],
			'hot dog': [],
			'sausage': [],
			'chicken': []}


tools = ["baking sheet","blender","bowl","box grater","brush","can opener","cast iron skillet",
		"colander","cutting board","double boiler","dutch oven","foil","food processer ","fork","frying pan",
		"funnel","garlic press","grill","hand mixer","knife","ladel","mandoline","measuring cup","microplane", 
		"mortar","paper towel","parchment paper","paring knife","peeler","pesltle","plastic wrap","plate","pot",
		"rack",'ramekin',"roasting pan","rolling pin","saucepan","sheet pan","sieve","skewer","skillet","smoker",
		"spatula","spoon","stand mixer","stock pot","thermometer","timer","tongs","twine","whisk", "sifter", "strainer", "mallet"]

primary_methods = ["bake","barbeque","boil","broil","braise","carmelize","flambe","fry","grill",
					"parbake","parboil","poach","roast","sear", "smoke","steam","saute", "sauté" "simmer",
					"stir fry","stew","sweat","toast", "baste", "melt", "reduce", "render", "temper"]

secondary_methods = ["arange","add","heat","brown","beat","blache","heat","cover","chop","combine",
					"crush","cube","cut","deglaze","dice","form", "fold","grind","julienne" ,"knead","mince","mix",
					"pound","preheat","pour","roll","rub","season","shredd","skewer","slice","stir","transfer","tenderize","whisk",
					"spoon", "drain", "sprinkle", "top", "layer", "lay", "place", "set", "strain", "line", "oil", "butter", "prepare"
					"refrigerate", "arrange", "turn", "flip", "brush", "galze", "dip" , "spread", "press", "coat", "pat", "save", "reserve",
					"put", "return", "scrape", "peel", "rinsed" "remove", "repeat", "allow". "rest", "toss", "distribute", "wash", "fill",
					"mash", "smash", "blend", "cool", "store", "cream", "drop", "dissolve"]

units = ["bag","teaspoon","tablespoon","ounce","clove","cup","pint","quart","gallon",
		"milliliter","liter","pound","gram","milligram","kilogram","pinch", "pinches", "handful","head",
		"loaf","loaves","can","package", "pack","bunch","bushel","T","tsp",'t',"tbl","tbsp",'tbs','c','p','gal','g']

preparations = ["chopped","shredded","ground","crushed","sliced","cooked","pureed",
				"peeled","smoked","minced","rinsed","trimmed","uncooked","rolled","pounded","cut","diced", "halved"]

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
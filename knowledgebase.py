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







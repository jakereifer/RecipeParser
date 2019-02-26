import pandas as pd
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

# not case sensitive
meats = [ Ingredient(name="bacon"), Ingredient(name="beef"), Ingredient(name="bison"), Ingredient(name="blood"), Ingredient(name="chicken"),Ingredient(name="chorizo"), Ingredient(name="cornish game hen"),
			Ingredient(name="duck"), Ingredient(name="foie gras"), Ingredient(name="game"), Ingredient(name="giblets"), Ingredient(name="goat"),
			Ingredient(name="goose"), Ingredient(name="guinea pig"), Ingredient(name="ham"), Ingredient(name="hedgehog"), Ingredient(name="horse"),
			Ingredient(name="hot dog"), Ingredient(name="kidney"), Ingredient(name="kielbasa"), Ingredient(name="lamb"), Ingredient(name="liver"),
			Ingredient(name="mortadella"), Ingredient(name="mutton"), Ingredient(name="neck sweetbread"), Ingredient(name="organ meat"),
			Ingredient(name="ostrich"), Ingredient(name="pancetta"), Ingredient(name="pastrami"), Ingredient(name="pepperoni"), Ingredient(name="pork"),
			Ingredient(name="prosciutto"), Ingredient(name="quail"), Ingredient(name="rabbit"), Ingredient(name="salami"), Ingredient(name="sausage"),
			Ingredient(name="sausage casing"), Ingredient(name="squirrel"), Ingredient(name="stomach sweetbread"),
			Ingredient(name="sweetbread"), Ingredient(name="tongue"), Ingredient(name="tripe"), Ingredient(name="turkey"), Ingredient(name="veal"), Ingredient(name="venison"), Ingredient(name="burger"), Ingredient(name="meatballs")]

# not case sensitive
seafood= [ Ingredient(name="salmon"), Ingredient(name="cod"), Ingredient(name="halibut"), Ingredient(name="mahi mahi"), Ingredient(name="tuna"), Ingredient(name="shark"),
			Ingredient(name="swordfish"), Ingredient(name="sturgeon"), Ingredient(name="catfish"), Ingredient(name="trout"), Ingredient(name="sardine"), 
			Ingredient(name="anchovy"), Ingredient(name="arctic char"), Ingredient(name="crab"), Ingredient(name="crayfish"), Ingredient(name="lobster"), 
			Ingredient(name="shrimp"), Ingredient(name="molluscs"), Ingredient(name="abalone"), Ingredient(name="clam"), Ingredient(name="cockle"), Ingredient(name="mussel"),
			Ingredient(name="octopus"), Ingredient(name="oyster"), Ingredient(name="pipi"), Ingredient(name="snail"), Ingredient(name="conch"), Ingredient(name="whelk"),
			Ingredient(name="winkle"), Ingredient(name="squid"), Ingredient(name="calamari"), Ingredient(name="scallop"), Ingredient(name="caviar"), Ingredient(name="uni"),
			Ingredient(name="sea cucumber"), Ingredient(name="hagfish"), Ingredient(name="tuna"), Ingredient(name="ikura")]

#veg_proteins
veg_proteins = [ Ingredient(name='tofu'), Ingredient(name='tempeh'), Ingredient(name='seitan'), Ingredient(name='jackfruit'), Ingredient(name='lentils'), Ingredient(name='beans'),
				Ingredient(name='legumes'), Ingredient(name='texturized vegetable protein (TVP)'),#tvp
				Ingredient(name='chickpeas'), Ingredient(name='falafel'), Ingredient(name='nuts'), Ingredient(name='soy'), Ingredient(name='vegetarian bacon'), Ingredient(name='veggie burger'),
				Ingredient(name='tofurkey'), Ingredient(name='veggie dog dog'), Ingredient(name='quinoa')]

meat_subs = { Ingredient(name='hamburger'): [Ingredient(name='veggie burger'), Ingredient(name='black bean burger')],
				Ingredient(name='meatball'): [Ingredient(name='veggie meatballs')],
				Ingredient(name='hot dog'): [Ingredient(name='veggie dog')],
				Ingredient(name='sausage'): [Ingredient(name='veggie sausage'), Ingredient(name='tempeh')],
				Ingredient(name='chicken'): [Ingredient(name='chick\'n'), Ingredient(name='tofu'), Ingredient(name='seitan')],
				Ingredient(name='default'): [Ingredient(name='tofu'), Ingredient(name="texturized vegetable protein (TVP)")],
				Ingredient(name='pork'): [Ingredient(name='seitan')],
				Ingredient(name='turkey'): [Ingredient(name='tofurkey')],
				Ingredient(name='beef'): [Ingredient(name='tofu'), Ingredient(name='seitan')],
				Ingredient(name='fish'): [Ingredient(name='tofu')],
				Ingredient(name='chorizo'): [Ingredient(name='beans')]
				}







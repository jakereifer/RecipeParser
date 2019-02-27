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
meats = [ Ingredient(name="bacon", category="protein", subcategory="meat"), Ingredient(name="beef", category="protein", subcategory="meat"), Ingredient(name="bison", category="protein", subcategory="meat"), Ingredient(name="blood", category="protein", subcategory="meat"), Ingredient(name="chicken", category="protein", subcategory="meat"),Ingredient(name="chorizo", category="protein", subcategory="meat"), Ingredient(name="cornish game hen", category="protein", subcategory="meat"),
			Ingredient(name="duck", category="protein", subcategory="meat"), Ingredient(name="foie gras", category="protein", subcategory="meat"), Ingredient(name="game", category="protein", subcategory="meat"), Ingredient(name="giblets", category="protein", subcategory="meat"), Ingredient(name="goat", category="protein", subcategory="meat"),
			Ingredient(name="goose", category="protein", subcategory="meat"), Ingredient(name="guinea pig", category="protein", subcategory="meat"), Ingredient(name="ham", category="protein", subcategory="meat"), Ingredient(name="hedgehog", category="protein", subcategory="meat"), Ingredient(name="horse", category="protein", subcategory="meat"),
			Ingredient(name="hot dog", category="protein", subcategory="meat"), Ingredient(name="kidney", category="protein", subcategory="meat"), Ingredient(name="kielbasa", category="protein", subcategory="meat"), Ingredient(name="lamb", category="protein", subcategory="meat"), Ingredient(name="liver", category="protein", subcategory="meat"),
			Ingredient(name="mortadella", category="protein", subcategory="meat"), Ingredient(name="mutton", category="protein", subcategory="meat"), Ingredient(name="neck sweetbread", category="protein", subcategory="meat"), Ingredient(name="organ meat", category="protein", subcategory="meat"),
			Ingredient(name="ostrich", category="protein", subcategory="meat"), Ingredient(name="pancetta", category="protein", subcategory="meat"), Ingredient(name="pastrami", category="protein", subcategory="meat"), Ingredient(name="pepperoni", category="protein", subcategory="meat"), Ingredient(name="pork", category="protein", subcategory="meat"),
			Ingredient(name="prosciutto", category="protein", subcategory="meat"), Ingredient(name="quail", category="protein", subcategory="meat"), Ingredient(name="rabbit", category="protein", subcategory="meat"), Ingredient(name="salami", category="protein", subcategory="meat"), Ingredient(name="sausage", category="protein", subcategory="meat"),
			Ingredient(name="sausage casing", category="protein", subcategory="meat"), Ingredient(name="squirrel", category="protein", subcategory="meat"), Ingredient(name="stomach sweetbread", category="protein", subcategory="meat"),
			Ingredient(name="sweetbread", category="protein", subcategory="meat"), Ingredient(name="tongue", category="protein", subcategory="meat"), Ingredient(name="tripe", category="protein", subcategory="meat"), Ingredient(name="turkey", category="protein", subcategory="meat"), Ingredient(name="veal", category="protein", subcategory="meat"), Ingredient(name="venison", category="protein", subcategory="meat"), Ingredient(name="burger", category="protein", subcategory="meat"), Ingredient(name="meatballs", category="protein", subcategory="meat")]

# not case sensitive
seafood= [ Ingredient(name="salmon", category="protein", subcategory="seafood"), Ingredient(name="cod", category="protein", subcategory="seafood"), Ingredient(name="halibut", category="protein", subcategory="seafood"), Ingredient(name="mahi mahi", category="protein", subcategory="seafood"), Ingredient(name="tuna", category="protein", subcategory="seafood"), Ingredient(name="shark", category="protein", subcategory="seafood"),
			Ingredient(name="swordfish", category="protein", subcategory="seafood"), Ingredient(name="sturgeon", category="protein", subcategory="seafood"), Ingredient(name="catfish", category="protein", subcategory="seafood"), Ingredient(name="trout", category="protein", subcategory="seafood"), Ingredient(name="sardine", category="protein", subcategory="seafood"), 
			Ingredient(name="anchovy", category="protein", subcategory="seafood"), Ingredient(name="arctic char", category="protein", subcategory="seafood"), Ingredient(name="crab", category="protein", subcategory="seafood"), Ingredient(name="crayfish", category="protein", subcategory="seafood"), Ingredient(name="lobster", category="protein", subcategory="seafood"), 
			Ingredient(name="shrimp", category="protein", subcategory="seafood"), Ingredient(name="molluscs", category="protein", subcategory="seafood"), Ingredient(name="abalone", category="protein", subcategory="seafood"), Ingredient(name="clam", category="protein", subcategory="seafood"), Ingredient(name="cockle", category="protein", subcategory="seafood"), Ingredient(name="mussel", category="protein", subcategory="seafood"),
			Ingredient(name="octopus", category="protein", subcategory="seafood"), Ingredient(name="oyster", category="protein", subcategory="seafood"), Ingredient(name="pipi", category="protein", subcategory="seafood"), Ingredient(name="snail", category="protein", subcategory="seafood"), Ingredient(name="conch", category="protein", subcategory="seafood"), Ingredient(name="whelk", category="protein", subcategory="seafood"),
			Ingredient(name="winkle", category="protein", subcategory="seafood"), Ingredient(name="squid", category="protein", subcategory="seafood"), Ingredient(name="calamari", category="protein", subcategory="seafood"), Ingredient(name="scallop", category="protein", subcategory="seafood"), Ingredient(name="caviar", category="protein", subcategory="seafood"), Ingredient(name="uni", category="protein", subcategory="seafood"),
			Ingredient(name="sea cucumber", category="protein", subcategory="seafood"), Ingredient(name="hagfish", category="protein", subcategory="seafood"), Ingredient(name="tuna", category="protein", subcategory="seafood"), Ingredient(name="ikura", category="protein", subcategory="seafood")]

dairy = [
		Ingredient(name="butter", category="protein", subcategory= "dairy")
		Ingredient(name="ghee", category="protein", subcategory= "dairy")
		Ingredient(name="buttermilk", category="protein", subcategory= "dairy")
		Ingredient(name="cheese", category="protein", subcategory= "dairy")
		Ingredient(name="cream", category="protein", subcategory= "dairy")
		Ingredient(name="sour cream", category="protein", subcategory= "dairy")
		Ingredient(name="whipped cream", category="protein", subcategory= "dairy")
		Ingredient(name="milk", category="protein", subcategory= "dairy")
		Ingredient(name="condensed milk", category="protein", subcategory= "dairy")
		Ingredient(name="yogurt", category="protein", subcategory= "dairy")
		Ingredient(name="lassi", category="protein", subcategory= "dairy")
		Ingredient(name="bohrani", category="protein", subcategory= "dairy")
		Ingredient(name="kefir", category="protein", subcategory= "dairy")
		Ingredient(name="egg", category="protein", subcategory= "dairy")
		Ingredient(name="egg white", category="protein", subcategory= "dairy")
		Ingredient(name="egg yolk", category="protein", subcategory= "dairy")]

#veg_proteins
veg_proteins = [ Ingredient(name="tofu", category="protein", subcategory="veg_protein"), Ingredient(name="tempeh", category="protein", subcategory="veg_protein"), Ingredient(name="seitan", category="protein", subcategory="veg_protein"), Ingredient(name="jackfruit", category="protein", subcategory="veg_protein"), Ingredient(name="lentils", category="protein", subcategory="veg_protein"), Ingredient(name="beans", category="protein", subcategory="veg_protein"),
				Ingredient(name="legumes", category="protein", subcategory="veg_protein"), Ingredient(name="texturized vegetable protein (TVP)", category="protein", subcategory="veg_protein"),#tvp
				Ingredient(name="chickpeas", category="protein", subcategory="veg_protein"), Ingredient(name="falafel", category="protein", subcategory="veg_protein"), Ingredient(name="nuts", category="protein", subcategory="veg_protein"), Ingredient(name="soy", category="protein", subcategory="veg_protein"), Ingredient(name="vegetarian bacon", category="protein", subcategory="veg_protein"), Ingredient(name="veggie burger", category="protein", subcategory="veg_protein"),
				Ingredient(name="tofurkey", category="protein", subcategory="veg_protein"), Ingredient(name="veggie dog", category="protein", subcategory="veg_protein"), Ingredient(name="quinoa", category="protein", subcategory="veg_protein"), Ingredient(name='chik\'n', category="protein", subcategory="veg_protein")]

meat_subs = { Ingredient(name='hamburger', category="protein", subcategory="meat"): [Ingredient(name='veggie burger', category="protein", subcategory="veg_protein"), Ingredient(name='black bean burger', category="protein", subcategory="veg_protein")],
				Ingredient(name='meatball', category="protein", subcategory="meat"): [Ingredient(name='veggie meatballs', category="protein", subcategory="veg_protein")],
				Ingredient(name='hot dog', category="protein", subcategory="meat"): [Ingredient(name='veggie dog', category="protein", subcategory="veg_protein")],
				Ingredient(name='sausage', category="protein", subcategory="meat"): [Ingredient(name='veggie sausage', category="protein", subcategory="veg_protein"), Ingredient(name='tempeh', category="protein", subcategory="veg_protein")],
				Ingredient(name='chicken', category="protein", subcategory="meat"): [Ingredient(name='chik\'n', category="protein", subcategory="veg_protein"), Ingredient(name='tofu', category="protein", subcategory="veg_protein"), Ingredient(name='seitan', category="protein", subcategory="veg_protein")],
				Ingredient(name='default', category="protein", subcategory="meat"): [Ingredient(name='tofu', category="protein", subcategory="veg_protein"), Ingredient(name="texturized vegetable protein (TVP)", category="protein", subcategory="veg_protein")],
				Ingredient(name='pork', category="protein", subcategory="meat"): [Ingredient(name='seitan', category="protein", subcategory="veg_protein")],
				Ingredient(name='turkey', category="protein", subcategory="meat"): [Ingredient(name='tofurkey', category="protein", subcategory="veg_protein")],
				Ingredient(name='beef', category="protein", subcategory="meat"): [Ingredient(name='tofu', category="protein", subcategory="veg_protein"), Ingredient(name='seitan', category="protein", subcategory="veg_protein")],
				Ingredient(name='fish', category="protein", subcategory="meat"): [Ingredient(name='tofu', category="protein", subcategory="veg_protein")],
				Ingredient(name='chorizo', category="protein", subcategory="meat"): [Ingredient(name='beans', category="protein", subcategory="veg_protein")]
			}

proteins = meats + seafood + veg_proteins + dairy

# REGEX: get before new line (.*)(\n)
# replace: Ingredient(name="\1", category="healthy", subcategory="vegetable"),\2

vegetables = [Ingredient(name="Alfalfa sprouts", category="healthy", subcategory="vegetable"),
Ingredient(name="Anise", category="healthy", subcategory="vegetable"),
Ingredient(name="Artichoke", category="healthy", subcategory="vegetable"),
Ingredient(name="Arugula", category="healthy", subcategory="vegetable"),
Ingredient(name="Asparagus", category="healthy", subcategory="vegetable"),
Ingredient(name="Aubergine", category="healthy", subcategory="vegetable"),
Ingredient(name="Avocado", category="healthy", subcategory="vegetable"),
Ingredient(name="Brassicas", category="healthy", subcategory="vegetable"),
Ingredient(name="Broccoflower", category="healthy", subcategory="vegetable"),
Ingredient(name="Broccoli", category="healthy", subcategory="vegetable"),
Ingredient(name="Broccolini", category="healthy", subcategory="vegetable"),
Ingredient(name="Broccoli rabe", category="healthy", subcategory="vegetable"),
Ingredient(name="Brussels sprouts", category="healthy", subcategory="vegetable"),
Ingredient(name="Cabbage", category="healthy", subcategory="vegetable"),
Ingredient(name="Cauliflower", category="healthy", subcategory="vegetable"),
Ingredient(name="Romanesco broccoli", category="healthy", subcategory="vegetable"),
Ingredient(name="Yu choy", category="healthy", subcategory="vegetable"),
Ingredient(name="Choy sum", category="healthy", subcategory="vegetable"),
Ingredient(name="Bok choy", category="healthy", subcategory="vegetable"),
Ingredient(name="Nappa cabbage", category="healthy", subcategory="vegetable"),
Ingredient(name="Collard greens", category="healthy", subcategory="vegetable"),
Ingredient(name="Kohlrabi", category="healthy", subcategory="vegetable"),
Ingredient(name="Breadfruit", category="healthy", subcategory="vegetable"),
Ingredient(name="Cactus pad", category="healthy", subcategory="vegetable"),
Ingredient(name="Calabrese", category="healthy", subcategory="vegetable"),
Ingredient(name="Celery", category="healthy", subcategory="vegetable"),
Ingredient(name="Chard", category="healthy", subcategory="vegetable"),
Ingredient(name="Chicory", category="healthy", subcategory="vegetable"),
Ingredient(name="Cucumber", category="healthy", subcategory="vegetable"),
Ingredient(name="Eggplant", category="healthy", subcategory="vegetable"),
Ingredient(name="Endive", category="healthy", subcategory="vegetable"),
Ingredient(name="Edible cactus", category="healthy", subcategory="vegetable"),
Ingredient(name="Fennel", category="healthy", subcategory="vegetable"),
Ingredient(name="Fiddlehead", category="healthy", subcategory="vegetable"),
Ingredient(name="Frisee", category="healthy", subcategory="vegetable"),
Ingredient(name="Hop shoot", category="healthy", subcategory="vegetable"),
Ingredient(name="Kale", category="healthy", subcategory="vegetable"),
Ingredient(name="Kangkung", category="healthy", subcategory="vegetable"),
Ingredient(name="Soybeans", category="healthy", subcategory="vegetable"),
Ingredient(name="Garlic", category="healthy", subcategory="vegetable"),
Ingredient(name="Winter leeks", category="healthy", subcategory="vegetable"),
Ingredient(name="Legume", category="healthy", subcategory="vegetable"),
Ingredient(name="Azuki bean", category="healthy", subcategory="vegetable"),
Ingredient(name="Beansprouts", category="healthy", subcategory="vegetable"),
Ingredient(name="Black beans", category="healthy", subcategory="vegetable"),
Ingredient(name="Black-eyed peas", category="healthy", subcategory="vegetable"),
Ingredient(name="Borlotti beans", category="healthy", subcategory="vegetable"),
Ingredient(name="Broad beans", category="healthy", subcategory="vegetable"),
Ingredient(name="Chickpea", category="healthy", subcategory="vegetable"),
Ingredient(name="Green beans", category="healthy", subcategory="vegetable"),
Ingredient(name="Red kidney bean", category="healthy", subcategory="vegetable"),
Ingredient(name="Lentils", category="healthy", subcategory="vegetable"),
Ingredient(name="Lima beans", category="healthy", subcategory="vegetable"),
Ingredient(name="Mung beans", category="healthy", subcategory="vegetable"),
Ingredient(name="Navy beans", category="healthy", subcategory="vegetable"),
Ingredient(name="Runner bean", category="healthy", subcategory="vegetable"),
Ingredient(name="Soybean", category="healthy", subcategory="vegetable"),
Ingredient(name="Pea", category="healthy", subcategory="vegetable"),
Ingredient(name="Mangetout", category="healthy", subcategory="vegetable"),
Ingredient(name="Snap pea", category="healthy", subcategory="vegetable"),
Ingredient(name="Lemongrass", category="healthy", subcategory="vegetable"),
Ingredient(name="Lettuce Lactuca sativa", category="healthy", subcategory="vegetable"),
Ingredient(name="Corn", category="healthy", subcategory="vegetable"),
Ingredient(name="Mangetout", category="healthy", subcategory="vegetable"),
Ingredient(name="Mustard green", category="healthy", subcategory="vegetable"),
Ingredient(name="Nettles", category="healthy", subcategory="vegetable"),
Ingredient(name="New Zealand spinach", category="healthy", subcategory="vegetable"),
Ingredient(name="Nori", category="healthy", subcategory="vegetable"),
Ingredient(name="Okra", category="healthy", subcategory="vegetable"),
Ingredient(name="Onion family", category="healthy", subcategory="vegetable"),
Ingredient(name="Chives", category="healthy", subcategory="vegetable"),
Ingredient(name="Garlic", category="healthy", subcategory="vegetable"),
Ingredient(name="Onion", category="healthy", subcategory="vegetable"),
Ingredient(name="Shallot", category="healthy", subcategory="vegetable"),
Ingredient(name="scallion ", category="healthy", subcategory="vegetable"),
Ingredient(name="shallot", category="healthy", subcategory="vegetable"),
Ingredient(name="Parsley", category="healthy", subcategory="vegetable"),
Ingredient(name="Daikon", category="healthy", subcategory="vegetable"),
Ingredient(name="Potatoes", category="healthy", subcategory="vegetable"),
Ingredient(name="Pepper", category="healthy", subcategory="vegetable"),
Ingredient(name="Bell pepper", category="healthy", subcategory="vegetable"),
Ingredient(name="Chili pepper", category="healthy", subcategory="vegetable"),
Ingredient(name="Radicchio", category="healthy", subcategory="vegetable"),
Ingredient(name="Rhubarb", category="healthy", subcategory="vegetable"),
Ingredient(name="Root vegetables", category="healthy", subcategory="vegetable"),
Ingredient(name="Beet", category="healthy", subcategory="vegetable"),
Ingredient(name="Carrot", category="healthy", subcategory="vegetable"),
Ingredient(name="Cassava", category="healthy", subcategory="vegetable"),
Ingredient(name="Celeriac", category="healthy", subcategory="vegetable"),
Ingredient(name="Daikon", category="healthy", subcategory="vegetable"),
Ingredient(name="Ginger", category="healthy", subcategory="vegetable"),
Ingredient(name="Sunchoke ", category="healthy", subcategory="vegetable"),
Ingredient(name="Jicama", category="healthy", subcategory="vegetable"),
Ingredient(name="Parsnip", category="healthy", subcategory="vegetable"),
Ingredient(name="Potato", category="healthy", subcategory="vegetable"),
Ingredient(name="Radish", category="healthy", subcategory="vegetable"),
Ingredient(name="Skirret", category="healthy", subcategory="vegetable"),
Ingredient(name="Rutabaga ", category="healthy", subcategory="vegetable"),
Ingredient(name="Sweet potato ", category="healthy", subcategory="vegetable"),
Ingredient(name="Taro root", category="healthy", subcategory="vegetable"),
Ingredient(name="Turnip", category="healthy", subcategory="vegetable"),
Ingredient(name="Wasabi", category="healthy", subcategory="vegetable"),
Ingredient(name="Water chestnut", category="healthy", subcategory="vegetable"),
Ingredient(name="White radish", category="healthy", subcategory="vegetable"),
Ingredient(name="Yam", category="healthy", subcategory="vegetable"),
Ingredient(name="Samphire", category="healthy", subcategory="vegetable"),
Ingredient(name="Silverbeet", category="healthy", subcategory="vegetable"),
Ingredient(name="Snap pea", category="healthy", subcategory="vegetable"),
Ingredient(name="Spinach", category="healthy", subcategory="vegetable"),
Ingredient(name="Squash family", category="healthy", subcategory="vegetable"),
Ingredient(name="Acorn squash", category="healthy", subcategory="vegetable"),
Ingredient(name="Bitter melon", category="healthy", subcategory="vegetable"),
Ingredient(name="Butternut squash", category="healthy", subcategory="vegetable"),
Ingredient(name="Calabaza", category="healthy", subcategory="vegetable"),
Ingredient(name="Chayote", category="healthy", subcategory="vegetable"),
Ingredient(name="Cucumber", category="healthy", subcategory="vegetable"),
Ingredient(name="Gem squash", category="healthy", subcategory="vegetable"),
Ingredient(name="Patty pan squash", category="healthy", subcategory="vegetable"),
Ingredient(name="Pumpkin", category="healthy", subcategory="vegetable"),
Ingredient(name="Spaghetti squash", category="healthy", subcategory="vegetable"),
Ingredient(name="Zucchini", category="healthy", subcategory="vegetable"),
Ingredient(name="Tomato", category="healthy", subcategory="vegetable"),
Ingredient(name="Tat soi", category="healthy", subcategory="vegetable"),
Ingredient(name="Tomatillo", category="healthy", subcategory="vegetable"),
Ingredient(name="Tomato", category="healthy", subcategory="vegetable"),
Ingredient(name="Watercress", category="healthy", subcategory="vegetable")]


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
					"spoon", "drain", "sprinkle", "top", "layer", "lay", "place", "set", "strain", "line", "oil", "butter", "prepare"
					"refrigerate", "arrange", "turn", "flip", "brush", "galze", "dip" , "spread", "press", "coat", "pat", "save", "reserve",
					"put", "return", "scrape", "peel", "rinsed" "remove", "repeat", "allow". "rest", "toss", "distribute", "wash", "fill",
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
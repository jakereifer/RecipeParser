import pandas as pd
from pprint import pprint
from RecipeClass import *
from IngredientClass import *
from SubstituteClass import *

# class Substitute(object):
# 	canreplace = []
# 	methods = {}
# 	quantity = {}
# 	tools = {}
	
	
# 	def __init__(self, canreplace=[], methods={}, quantity={}, tools={}):
# 		self.canreplace = canreplace
# 		self.methods = methods
# 		self.quantity = quantity
# 		self.tools = tools
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
	Ingredient(name="abalone", tags=[1,6]),
	Ingredient(name="anchovy", tags=[1,4]),
	Ingredient(name="all-purpose flour", tags=[4]),
	Ingredient(name="almond milk", tags=[3]),
	Ingredient(name="arctic char", tags=[1]),
	Ingredient(name="bacon", tags=[1,4,6]),
	Ingredient(name="barbeque sauce", tags=[5]),
	Ingredient(name="basil", tags=["seasoning"]),
	Ingredient(name="bass", tags=[]),
	Ingredient(name="beans", tags=[]),
	Ingredient(name="beef", tags=[1,4,"meat"]),
	Ingredient(name="beef broth", tags=[1,"meat"]),
	Ingredient(name="bell pepper", tags=[5]),
	Ingredient(name="bergall", tags=[]),
	Ingredient(name="bison", tags=[1,"meat"]),
	Ingredient(name="blood", tags=[1,6]),
	Ingredient(name="bologna", tags=[1,6]),
	Ingredient(name="brown rice", tags=[3]),
	Ingredient(name="burger", tags=[1,4,"meat"]),
	Ingredient(name="butter", tags=[4,"dairy"]),
	Ingredient(name="buttermilk", tags=[4,"dairy"]),
	Ingredient(name="cacao nibs", tags=[3]),
	Ingredient(name="calamari", tags=[1,4,6]),
	Ingredient(name="catfish", tags=[1,6]),
	Ingredient(name="caviar", tags=[1,6]),
	Ingredient(name="cayenne pepper", tags=["seasoning"]),
	Ingredient(name="cheese", tags=[5,"dairy"]),
	Ingredient(name="chicken", tags=[1,3,"meat"]),
	Ingredient(name="chicken broth", tags=[1,"meat"]),
	Ingredient(name="chicken stock", tags=[1,"meat"]),
	Ingredient(name="chickpeas", tags=[]),
	Ingredient(name="chik'n", tags=[2]),
	Ingredient(name="chocolate chips", tags=[4]),
	Ingredient(name="chorizo", tags=[1,4,6]),
	Ingredient(name="cinnamon", tags=["seasoning"]),
	Ingredient(name="clam", tags=[1,6]),
	Ingredient(name="cocoa powder", tags=[3]),
	Ingredient(name="coconut milk", tags=[3]),
	Ingredient(name="cod", tags=[1,3,6]),
	Ingredient(name="conch", tags=[1,6]),
	Ingredient(name="condensed milk", tags=[4,"dairy"]),
	Ingredient(name="corn tortilla", tags=[3]),
	Ingredient(name="cornish game hen", tags=[1,"meat"]),
	Ingredient(name="crab", tags=[1,6]),
	Ingredient(name="crayfish", tags=[1,6]),
	Ingredient(name="cream", tags=[4]),
	Ingredient(name="curry powder", tags=["seasoning"]),
	Ingredient(name="deer", tags=[]),
	Ingredient(name="duck", tags=[1,"meat"]),
	Ingredient(name="eel", tags=[6]),
	Ingredient(name="egg", tags=[]),
	Ingredient(name="egg white", tags=[3]),
	Ingredient(name="egg yolk", tags=[4]),
	Ingredient(name="elk", tags=[]),
	Ingredient(name="falafel", tags=[2]),
	Ingredient(name="filet mignon steak", tags=[]),
	Ingredient(name="fish", tags=[1,3]),
	Ingredient(name="flounder", tags=[]),
	Ingredient(name="flour tortilla", tags=[4]),
	Ingredient(name="foie gras", tags=[1,4,"meat"]),
	Ingredient(name="garam masala", tags=["seasoning"]),
	Ingredient(name="gelatin", tags=[6]),
	Ingredient(name="ginger", tags=["seasoning"]),
	Ingredient(name="goat", tags=[1,4,"meat"]),
	Ingredient(name="goose", tags=[1,4,"meat"]),
	Ingredient(name="green pepper", tags=[5]),
	Ingredient(name="ground beef", tags=[1,4,"meat"]),
	Ingredient(name="halibut", tags=[1,3]),
	Ingredient(name="ham", tags=[1,4,6]),
	Ingredient(name="hamburger", tags=[1,4,"meat"]),
	Ingredient(name="hot dog", tags=[1,4,6]),
	Ingredient(name="lamb", tags=[1,4,"meat"]),
	Ingredient(name="legumes", tags=[2,3]),
	Ingredient(name="lemon juice", tags=[5]),
	Ingredient(name="lemon zest", tags=[5]),
	Ingredient(name="lentils", tags=[2]),
	Ingredient(name="liver", tags=[1,4,"meat"]),
	Ingredient(name="lobster", tags=[1,6]),
	Ingredient(name="mackerel", tags=[]),
	Ingredient(name="mahi mahi", tags=[1,3]),
	Ingredient(name="mahi-mahi", tags=[]),
	Ingredient(name="margarine", tags=[3]),
	Ingredient(name="marinara sauce", tags=[5]),
	Ingredient(name="meatballs", tags=[1,4,"meat"]),
	Ingredient(name="meatless meatballs", tags=[2,3]),
	Ingredient(name="milk", tags=[4,"dairy"]),
	Ingredient(name="mortadella", tags=[1,6]),
	Ingredient(name="mussel", tags=[1,6]),
	Ingredient(name="mutton", tags=[1,"meat"]),
	Ingredient(name="neck sweetbread", tags=[1,"meat"]),
	Ingredient(name="nutmeg", tags=["seasoning"]),
	Ingredient(name="octopus", tags=[1,6]),
	Ingredient(name="olive oil", tags=[3]),
	Ingredient(name="organ meat", tags=[1,6]),
	Ingredient(name="ostrich", tags=[1,"meat"]),
	Ingredient(name="oyster", tags=[6]),
	Ingredient(name="pancetta", tags=[1,4,6]),
	Ingredient(name="pasta", tags=[4]),
	Ingredient(name="pastrami", tags=[1,4,"meat"]),
	Ingredient(name="pepperoni", tags=[1,4,6]),
	Ingredient(name="pesto", tags=[5]),
	Ingredient(name="pig", tags=[1,6]),
	Ingredient(name="pork", tags=[1,4,6]),
	Ingredient(name="prosciutto", tags=[1,4,6]),
	Ingredient(name="quail", tags=[1,"meat"]),
	Ingredient(name="quinoa", tags=[3]),
	Ingredient(name="rabbit", tags=[1,"meat"]),
	Ingredient(name="rosemary", tags=["seasoning"]),
	Ingredient(name="sage", tags=["seasoning"]),
	Ingredient(name="salami", tags=[1,6]),
	Ingredient(name="sardine", tags=[1]),
	Ingredient(name="sausage", tags=[1,4,6]),
	Ingredient(name="sausage casing", tags=[1,6]),
	Ingredient(name="scallop", tags=[1,3,6]),
	Ingredient(name="sea cucumber", tags=[1,6]),
	Ingredient(name="seitan", tags=[2,3]),
	Ingredient(name="shark", tags=[1,6]),
	Ingredient(name="shrimp", tags=[1,3,6]),
	Ingredient(name="snapper", tags=[1]),
	Ingredient(name="sour cream", tags=[4,"dairy"]),
	Ingredient(name="squid", tags=[1,3,6]),
	Ingredient(name="steak", tags=[1,4,"meat"]),
	Ingredient(name="stevia", tags=[3]),
	Ingredient(name="stomach sweetbread", tags=[1,"meat"]),
	Ingredient(name="sturgeon", tags=[1,6]),
	Ingredient(name="sugar", tags=[4]),
	Ingredient(name="sweetbread", tags=[1,"meat"]),
	Ingredient(name="swordfish", tags=[1,6]),
	Ingredient(name="tempeh", tags=[2,3]),
	Ingredient(name="texturized vegetable protein (tvp)", tags=[2,3]),
	Ingredient(name="thyme", tags=["seasoning"]),
	Ingredient(name="tilapia", tags=[1]),
	Ingredient(name="tofu", tags=[2,3]),
	Ingredient(name="tofurky", tags=[2,3]),
	Ingredient(name="tongue", tags=[1,"meat"]),
	Ingredient(name="tortilla", tags=[4]),
	Ingredient(name="trout", tags=[1]),
	Ingredient(name="tuna", tags=[1,4]),
	Ingredient(name="turkey", tags=[1,3,"meat"]),
	Ingredient(name="turkey bacon", tags=[1,3,"meat"]),
	Ingredient(name="turkey burger", tags=[1,3,"meat"]),
	Ingredient(name="turkey meatballs", tags=[1,3,"meat"]),
	Ingredient(name="turmeric", tags=["seasoning"]),
	Ingredient(name="veal", tags=[1,"meat"]),
	Ingredient(name="vegetable broth", tags=[2]),
	Ingredient(name="vegetable stock", tags=[2]),
	Ingredient(name="vegetarian burger", tags=[2,3]),
	Ingredient(name="veggie bacon strips", tags=[2,3]),
	Ingredient(name="veggie burger", tags=[2,3]),
	Ingredient(name="veggie dog", tags=[2]),
	Ingredient(name="veggie meatballs", tags=[2]),
	Ingredient(name="veggie sausage", tags=[2]),
	Ingredient(name="venison", tags=[1,"meat"]),
	Ingredient(name="whipped cream", tags=[4,"dairy"]),
	Ingredient(name="white bread", tags=[4]),
	Ingredient(name="white rice", tags=[4]),
	Ingredient(name="whitefish", tags=[]),
	Ingredient(name="whole wheat flour", tags=[3]),
	Ingredient(name="whole wheat pasta", tags=[3]),
	Ingredient(name="yellow pepper", tags=[5]),
	Ingredient(name="yogurt", tags=[3,"dairy"])
]
	



substitute_map= {
1:{
"beans": Substitute(canreplace=["bologna","ground pork", "chorizo"], quantity={"default": (.5, "cup")}),
"chik'n": Substitute(canreplace=["crayfish", "cornish game hen","chicken", "ostrich", "quail", "rabbit", "neck sweetbread", "mutton","goose"], quantity={"default": (7, "grams")}),
"falafel": Substitute(canreplace=["gyro", "lamb"], quantity={"default": (3.5, "ounces")}),
"seitan": Substitute(canreplace=["conch","arctic char","catfish","anchovy","abalone","duck", "lobster", "shrimp", "calamari", "foie gras", "pastrami", "squid", "pig", "octopus"], quantity={"default": (.66, "cup")}),
"tempeh": Substitute(canreplace=["blood","bison","beef", "steak", "veal", "crab", "venison", "tongue", "tilapia", "swordfish", "sweetbread", "sturgeon", "stomach sweetbread", "liver"], quantity={"default": (3, "ounces")}),
"texturized vegetable protein (TVP)": Substitute(canreplace=["default", "ham", "goat"], quantity={"default": (.25, "cup")}),
"tofu": Substitute(canreplace=["fish", "caviar","clam","cod","halibut","ikura","mussel","mahi mahi","salmon","scallop","trout","tuna", "organ meat", "pork","sardine","sea cucumber","shark","snapper"], quantity={"default": (.75, "cup")}),
"tofurky": Substitute(canreplace=["turkey", "mortadella"], quantity={"default": (5, "slices")}),
"veggie bacon strips": Substitute(canreplace=["bacon", "pancetta", "prosciutto", "turkey bacon", "sausage casing"], quantity={"default": (16, "grams")}),
"veggie burger": Substitute(canreplace=["burger", "hamburger", "turkey burger"], quantity={"default": (1, "count")}),
"veggie dog": Substitute(canreplace=["hot dog"], quantity={"default": (1, "count")}),
"vegetable stock": Substitute(canreplace=["chicken stock"], quantity={"default": (1, "cup")}),
"vegetable broth": Substitute(canreplace=["chicken broth", "beef broth"], quantity={"default": (1, "cup")}),
"meatless meatballs": Substitute(canreplace=["meatballs", "ground beef", "turkey meatballs"], quantity={"default": (60, "gram")}),
"veggie sausage": Substitute(canreplace=["sausage", "pepperoni","salami"], quantity={"default": (.125, "pound")})
},
2:{
"bacon": Substitute(canreplace=["veggie bacon strips"], quantity={"default":(15,"grams")}),
"beef": Substitute(canreplace=["seitan", "tempeh"], quantity={"default":(4,"ounces")}),
"hamburger": Substitute(canreplace=["veggie burger", "vegetarian burger"], quantity={"default":(1,"count")}),
"chicken": Substitute(canreplace=["chik'n", "tofu","legumes"], quantity={"default":(4,"ounces")}),
"chicken broth": Substitute(canreplace=["vegetable broth"], quantity={"default":(1,"cup")}),
"chicken stock": Substitute(canreplace=["vegetable stock"], quantity={"default":(1,"cup")}),
"ground beef": Substitute(canreplace=["texturized vegetable protein (tvp)", "falafel","lentils"], quantity={"default":(4,"ounces")}),
"hot dog": Substitute(canreplace=["veggie dog"], quantity={"default":(1,"count")}),
"meatballs": Substitute(canreplace=["veggie meatballs", "meatless meatballs"], quantity={"default":(3,"ounces")}),
"turkey": Substitute(canreplace=["tofurky"], quantity={"default":(3.5,"ounces")}),
"sausage": Substitute(canreplace=["veggie sausage"], quantity={"default":(3.5,"ounces")})
},
3:{
"buttermilk": Substitute(canreplace=["almond milk", "coconut milk"], quantity={"default":(1,"cup")}),
"white rice": Substitute(canreplace=["brown rice"], quantity={"default":(.25,"cups")}),
"chocolate chips": Substitute(canreplace=["cacao nibs", "cocoa powder","legumes"], quantity={"default":(.25,"cup")}),
"pork": Substitute(canreplace=["chicken"], quantity={"default":(3,"ounces")}),
"calamari": Substitute(canreplace=["cod","fish", "halibut", "mahi mahi", "salmon", "scallop", "shrimp", "squid"], quantity={"default":(3, "ounces")}),
"flour tortilla": Substitute(canreplace=["corn tortilla"], quantity={"default":(1,"count")}),
"egg yolk": Substitute(canreplace=["egg white"], quantity={"default":(1,"count")}),
"butter": Substitute(canreplace=["margarine", "oil", "olive oil"], quantity={"default":(1,"tablespoon")}),
"whole milk": Substitute(canreplace=["milk"], quantity={"default":(1,"cup")}),
"sugar": Substitute(canreplace=["stevia"], quantity={"default":(1,"teaspoon")}),
"ground beef": Substitute(canreplace=["tempeh","tofu", "texturized vegetable protein (tvp)", "seitan"], quantity={"default":(4,"ounces")}),
"hamburger": Substitute(canreplace=["turkey burger", "vegetarian burger", "veggie burger"], quantity={"default":(1,"count")}),
"meatballs": Substitute(canreplace=["turkey meatballs", "veggie meatballs", "meatless meatballs"], quantity={"default":(3,"count")}),
"ham": Substitute(canreplace=["turkey", "tofurky"], quantity={"default":(.25,"pounds")}),
"bacon": Substitute(canreplace=["veggie bacon strips", "turkey bacon"], quantity={"default":(15,"grams")}),
"hot dog": Substitute(canreplace=["veggie hot dog"], quantity={"default":(1,"count")}),
"white bread": Substitute(canreplace=["whole wheat bread"], quantity={"default":(1,"count")}),
"all-purpose flour": Substitute(canreplace=["whole wheat flour"], quantity={"default":(.25,"cups")}),
"pasta": Substitute(canreplace=["whole wheat pasta", "quinoa"], quantity={"default":(1,"cup")}),
"heavy cream": Substitute(canreplace=["yogurt","bohrani"], quantity={"default":(1,"tablespoon")})
},
4:{
"egg yolk": Substitute(canreplace=["egg yolk"], quantity={"default":(1,"count")}),
"cacao nibs": Substitute(canreplace=["chocolate chips"], quantity={"default":(.25,"cup")}),
"chicken": Substitute(canreplace=["anchovy","ground beef", "beef","steak","venison","veal","goat","goose","lamb", "liver"], quantity={"default": (4,"ounce")}),
"milk": Substitute(canreplace=["cream", "condensed milk", "buttermilk"], quantity={"default": (.25, "cup")}),
"Almond milk": Substitute(canreplace=["milk"], quantity={"default":(1, "cup")}),
"margarine": Substitute(canreplace=["butter"], quantity={"default": (1, "tablespoon")}),
"stevia": Substitute(canreplace=["sugar", "brown sugar"], quantity={"default": (1, "teaspoon")}),
"brown rice": Substitute(canreplace=["calamari","white rice"], quantity={"default": (.125, "cup")}),
"whole wheat flour": Substitute(canreplace=["flour", "all-purpose flour"], quantity={"default": (.125, "cup")}),
"turkey": Substitute(canreplace=["chorizo","pork", "pastrami","foie gras","ham"], quantity={"default": (3.5, "ounces")}),
"whole wheat bread": Substitute(canreplace=["bread", "white bread"], quantity={"default": (2, "count")}),
"whole wheat pasta": Substitute(canreplace=["pasta"], quantity={"default": (.5, "cup")}),
"turkey meatballs": Substitute(canreplace=["meatballs"], quantity={"default": (4, "count")}),
"turkey burger": Substitute(canreplace=["hamburger", "burger"], quantity={"default": (1, "count")}),
"turkey bacon": Substitute(canreplace=["bacon", "pancetta", "pepperoni", "prosciutto"], quantity={"default": (15, "grams")}),
"veggie sausage": Substitute(canreplace=["sausage","hot dog"], quantity={"default": (.125, "pound")}),
"salmon": Substitute(canreplace=["tuna"], quantity={"default": (2.5, "ounces")}),
"sugar-free whipped cream": Substitute(canreplace=["whipped cream"], quantity={"default":(2, "tablespoons")}),
"corn tortilla": Substitute(canreplace=["flour tortilla", "tortilla"], quantity={"default":(1,"count")}),
"low fat sour cream": Substitute(canreplace=["sour cream"], quantity={"default":(.25, "cup")})
},
5: {
"chili powder": Substitute(canreplace=["turmeric","basil","ginger","nutmeg","cinnamon", "curry powder", "cayenne pepper", "thyme", "rosemary", "sage"]),
"jalapeno ": Substitute(canreplace=["red pepper", "green pepper", "bell pepper", "yellow pepper"]),
"lime juice": Substitute(canreplace=["lemon juice", "lemon zest"]),
"salsa": Substitute(canreplace=["barbeque sauce", "marinara sauce", "pesto"]),
"cotija cheese": Substitute(canreplace=["cheese"])
},
"dairy": {
"almond milk": Substitute(canreplace=["milk", "buttermilk", "condensed milk"], quantity={"default":(1,"cup")}),
"margarine": Substitute(canreplace=["butter"], quantity={"default":(1,"tablespoon")}),
"vegan cheese": Substitute(canreplace=["cheese"], quantity={"default":(1,"ounce")}),
"almond yogurt": Substitute(canreplace=["yogurt"], quantity={"default":(.5,"cup")}),
"tofutti sour cream": Substitute(canreplace=["sour cream"], quantity={"default":(.25,"cup")}),
"non dairy reddi whip": Substitute(canreplace=["whipped cream"], quantity={"default":(1,"ounce")})
},
6: {
"seitan": Substitute(canreplace=["eel","abalone", "crab", "crayfish", "clam", "oyster", "calamari", "squid", "shrimp", "octopus", "mussel", "conch", "caviar", "scallop", "pipi"], quantity={"default":(4,"ounces")}),
"ground beef": Substitute(canreplace=["blood", "sea cucumber"], quantity={"default":(4,"ounces")}),
"chicken": Substitute(canreplace=["pork"], quantity={"default":(4,"ounces")}),
"turkey bacon": Substitute(canreplace=["bacon", "pig", "prosciutto", "pancetta", "mortadella"], quantity={"default":(4,"ounces")}),
"turkey sausage": Substitute(canreplace=["sausage", "pepperoni", "chorizo", "sausage casing"], quantity={"default":(4,"ounces")}),
"kosher hot dog": Substitute(canreplace=["hot dog"], quantity={"default":(1,"count")}),
"turkey": Substitute(canreplace=["bologna", "ham", "salami", "organ meat"], quantity={"default":(4,"ounces")}),
"salmon": Substitute(canreplace=["swordfish", "eel", "catfish", "cod", "shark","sturgeon","lobster"], quantity={"default":(4,"ounces")}),
"agar": Substitute(canreplace=["gelatin"], quantity={"default":(.5,"teaspoon")})
},
"seasoning": {},
"meat": {}


}














# """
# transformations_display = { 0: "None",
# 					1: "To vegetarian", # not vegetarian
# 					2: "From vegetarian", # vegetarian
# 					3: "From healthy", # healthy
# 					4: "To healthy", # unhealthy
# 					5: "To cuisine",
# 					6: "From cuisine" }


# 1: not vegetarian
# 2: vegetarian
# 3: healthy
# 4: unhealthy
# """

cs = [3, 4, 2, 1, "seasoning", 5, 6, "dairy", "meat"]
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

primary_methods = ["cook","bake","barbeque","boil","broil","braise","fry","grill","parbake","parboil","poach","roast","sear", "smoke","steam","saute", "sauté", "stir fry","stew",]

secondary_methods = ["simmer", "sweat","toast", "baste", "melt", "reduce", "render", "temper", "freeze", "clarify", "spray", "carmelize","flambe","serve","refrigerate","remove", "lift", "arange","add","heat","beat","blache","cover","chop","combine", "chill", "crush","cube","cut","deglaze","dice","form", "fold","grind","julienne" ,"knead","mince","mix","pound","preheat","pour","roll","rub","season","shredd","skewer","slice","stir","transfer","tenderize","whisk","spoon", "drain", "sprinkle", "top", "layer", "lay", "place", "set", "strain", "line", "prepare", "refrigerate", "arrange", "turn", "flip", "brush", "galze", "dip" , "spread", "press", "coat", "pat", "save", "reserve","put", "return", "scrape", "peel", "rinsed" "remove", "repeat", "allow","rest", "toss", "distribute", "wash", "fill","mash", "smash", "blend", "cool", "store", "drop", "dissolve"]

units = ["sprig","sprigs","bag","teaspoon","tablespoon","ounce","clove","cup","pint","quart","gallon", "milliliter","liter","pound","gram","milligram","kilogram","pinch", "pinches", "handful","head","loaf","loaves","can","package", "container", "pack","bunch","bushel","T","tsp",'t',"tbl","tbsp",'tbs','c','p','gal','g']

preparations = ["flavored","chopped","shredded","ground","crushed","sliced","cooked","pureed","peeled","smoked","minced","rinsed","trimmed","uncooked","rolled","pounded","cut","diced", "halved", "melted", "frozen", "clarified"]

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
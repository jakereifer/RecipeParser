import knowledgebase
class Ingredient(object):
	name = ""
	quantity = 0
	measurement = ""
	descriptor = ""
	preparation = ""

	def __init__(self, name="", quantity=0, measurement="", desc="", prep=""):
		self.name = name
		self.quantity = quantity,
		self.measurement = measurement
		self.descriptor = desc
		self.preparation = prep

# parses the ingredient (no descriptor yet) (works for most types)
def parseIngredient(i):
	# words of the ingredient
	i_words = i.split()
	ingredient = Ingredient()
	if len(i_words) == 1:
		ingredient.name = i_words[0]
		return ingredient
	# 2 eggs	
	if len(i_words) == 2:
		if i_words[0].isnumeric():
			ingredient.quantity = parse_amount(i_words[0])
			ingredient.name = i_words[1]
			ingredient.measurement = "count"
		return ingredient
	name = 0
	prep_dividers = [",", " - "]
	# last word index
	end = len(i_words)-1
	# Get the quantityquantity
	if i[0].isnumeric():
		ingredient.quantity = parse_amount(i_words[0])
		# print(ingredient.quantity)
	else:
		ingredient.name = i.strip()
		return ingredient
	# if there is an open parenthesis
	if i_words[1][0] == "(":
		for i in range(1,len(i_words)):
			if i_words[i][len(i_words[i])-1] == ")":
				ingredient.measurement = " ".join(i_words[1:i+2]).strip()
				name = i + 2
				break
		ingredient.name = " ".join(i_words[name:len(i_words)]).strip()
	else:
		if i_words[1][0].isnumeric() and len(i_words) > 3:
			ingredient.quantity = float(i_words[0]) + parse_amount(i_words[1])
			ingredient.measurement = i_words[2]
			ingredient.name = " ".join(i_words[3:len(i_words)]).strip()
		else:
			ingredient.measurement = i_words[1].strip()
			ingredient.name = " ".join(i_words[2:len(i_words)]).strip()
	
	#check to see if there are preparation instructions
	for pd in prep_dividers:
		if pd in ingredient.name:
			ingredient.preparation = ingredient.name.split(pd)[1].strip()
			ingredient.name = ingredient.name.split(pd)[0].strip()
	# trim whitespace
	return ingredient




# parse the amount needed in decimal
def parse_amount(amount_string):

	if "/" in amount_string:
		divisor = float(amount_string[0:amount_string.find("/")])
		dividend = float(amount_string[amount_string.find("/")+1:])
		amt = divisor/dividend
	else:
		amt = float(amount_string)


	return amt

# Print the ingredient in a human friendly manner
def printIngredient(i):
	if i.name:
		print("Name: ", i.name)
	if i.quantity:
		print("Quantity: ", i.quantity)
	if i.measurement:
		print("Measurement: ", i.measurement)
	if i.descriptor:
		print("Descriptor: ", i.descriptor)
	if i.preparation:
		print("Preparation: ", i.preparation)



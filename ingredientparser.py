import knowledgebase
<<<<<<< HEAD

class Ingredient(object):
	name = ""
	quantity = 0
	measurement = ""
	descriptor = ""
	preparation = ""
=======
from helpers import *
>>>>>>> 13945bca90c7de4cdf0a6ce1d214433908803e13

	def __init__(self, name="", quantity=0, measurement="", desc="", prep=""):
		self.name = name
		self.quantity = quantity
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
<<<<<<< HEAD
		if i_words[0][0].isnumeric():
			ingredient.quantity = i_words[0]
=======
		if i_words[0].isnumeric():
			ingredient.quantity = parse_amount(i_words[0])
>>>>>>> 13945bca90c7de4cdf0a6ce1d214433908803e13
			ingredient.name = i_words[1]
			ingredient.measurement = "count"
		else:
			ingredient.name = " ".join(i_words)
		return ingredient
	
	name = 0
	prep_dividers = [",", " - "]
<<<<<<< HEAD
	prep_words = knowledgebase.preparations
	unit_words = knowledgebase.units
	two_word_units = ["fluid ounce", "fl oz"]
	left_side = ""
	right_side = ""
	found_unit = False
	# search for units
	for i in range(0,len(i_words)):
		if found_unit:
			break
		for uw in unit_words:
			if i_words[i].lower() == uw:
				ingredient.measurement = uw
				found_unit = True
				left_side = (" ".join(i_words)).split(uw)[0]
				right_side = (" ".join(i_words)).split(uw)[1]
				break
			elif i_words[i].lower() == uw+'s':
				ingredient.measurement = uw
				found_unit = True
				left_side = (" ".join(i_words)).split(uw+'s')[0]
				right_side = (" ".join(i_words)).split(uw+'s')[1]
				break
		for twu in two_word_units:
			if i_words[i].lower() == twu.split()[0] and i+1 < len(i_words):
				if i_words[i+1].lower() == twu.split()[1]:
					ingredient.measurement = twu
					found_unit = True
					left_side = (" ".join(i_words)).split(twu)[0]
					right_side = (" ".join(i_words)).split(twu)[1]
					break
				if i_words[i+1].lower() == twu.split()[1]+'s':
					ingredient.measurement = twu
					found_unit = True
					left_side = (" ".join(i_words)).split(twu+'s')[0]
					right_side = (" ".join(i_words)).split(twu+'s')[1]
					break
	#if we didnt find a unit
	if not found_unit:
		if not i_words[0][0].isnumeric():
			ingredient.name = " ".join(i_words)
			left_side = ""
			right_side = ingredient.name
=======
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
>>>>>>> 13945bca90c7de4cdf0a6ce1d214433908803e13
		else:
			for i in range(1,len(i_words)):
				if not i_words[i][0].isnumeric():
					left_side = " ".join(i_words[:i])
					right_side = " ".join(i_words[i:])
					break
	#look at the left side
	left_side = left_side.strip()
	if '(' in left_side:
		ingredient.quantity = left_side.split('(')[0].strip()
		ingredient.measurement = '('+ left_side.split('(')[1].strip() + " " + ingredient.measurement
	else:
		ingredient.quantity = left_side.strip()
	#look at the right side
	right_side = right_side.strip()
	#look if there is preparation steps
	for pd in prep_dividers:
		if pd in right_side:
			ingredient.preparation = ", ".join(right_side.split(pd)[1:]).strip()
			ingredient.name = right_side.split(pd)[0].strip()
			right_side = ingredient.name
	rs_words = right_side.split()
	found_prep = False
	for i in range(0,len(rs_words)):
		if found_prep:
			break
		for pw in prep_words:
			if pw == rs_words[i]:
				found_prep = True
				if len(rs_words) > i+1:
					ingredient.name = " ".join(rs_words[i+1:])
				else:
					ingredient.name = rightside
					return ingredient
				if not ingredient.preparation == "":
					ingredient.preparation = ingredient.preparation + ", " + " ".join(rs_words[:i+1])
				else:
					ingredient.preparation = " ".join(rs_words[:i+1])
				break
	if not found_prep:
		ingredient.name = right_side
	return ingredient


<<<<<<< HEAD
=======


>>>>>>> 13945bca90c7de4cdf0a6ce1d214433908803e13
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

<<<<<<< HEAD
# x = "2 cloves garlic, minced"
# printIngredient(parseIngredient(x))
=======
	


>>>>>>> 13945bca90c7de4cdf0a6ce1d214433908803e13

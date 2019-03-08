import knowledgebase
from helpers import *
from IngredientClass import *

def parseIngredient(i):
	# words of the ingredient
	i_words = i.split()
	ingredient = Ingredient()
	if len(i_words) == 1:
		ingredient.name = i_words[0]
		ingredient.tags, ingredient.substitute = ingredientTagsAndSubs(ingredient)
		return ingredient
	# 2 eggs	
	if len(i_words) == 2:
		if i_words[0][0].isnumeric():
			ingredient.quantity = parse_amount(i_words[0])
			ingredient.name = i_words[1]
			ingredient.measurement = "count"
		else:
			ingredient.name = " ".join(i_words)

		ingredient.tags, ingredient.substitute = ingredientTagsAndSubs(ingredient)
		return ingredient
	
	name = 0
	prep_dividers = [",", " - "]
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
		else:
			for i in range(1,len(i_words)):
				if not i_words[i][0].isnumeric():
					left_side = " ".join(i_words[:i])
					right_side = " ".join(i_words[i:])
					break
	#look at the left side
	left_side = left_side.strip()
	if '(' in left_side:
		ingredient.quantity = parse_amount(left_side.split('(')[0].strip())
		ingredient.measurement = '('+ left_side.split('(')[1].strip() + " " + ingredient.measurement
	else:
		# print(left_side)
		ingredient.quantity = parse_amount(left_side.strip())
	#look at the right side
	right_side = right_side.strip()
	#look if there is preparation steps
	for pd in prep_dividers:
		if pd in right_side:
			if len(right_side.split(pd)) > 2:
				# print(right_side.split(pd))
				ingredient.preparation = ", ".join(right_side.split(pd)[2:]).strip()
				# print("THIS: ", "".join(right_side.split(pd)[0:2]).strip())
				ingredient.name = "".join(right_side.split(pd)[0:2]).strip()
				right_side = ingredient.name
				# print("name ", ingredient.name)
			else:
				ingredient.preparation = ", ".join(right_side.split(pd)[1:]).strip()
				ingredient.name = right_side.split(pd)[0].strip()
				right_side = ingredient.name
	rs_words = right_side.split()
	found_prep = False
	for i in range(0,len(rs_words)):
		if found_prep:
			break
		for pw in prep_words:
			if pw == rs_words[i] and not dontIncludeAsPrep(pw, rs_words[i:]):
				found_prep = True
				if len(rs_words) > i+1:
					ingredient.name = " ".join(rs_words[i+1:])
				else:
					ingredient.name = rightside
					ingredient.tags = ingredientTagsAndSubs(ingredient)
					return ingredient
				if not ingredient.preparation == "":
					ingredient.preparation = ingredient.preparation + ", " + " ".join(rs_words[:i+1])
				else:
					ingredient.preparation = " ".join(rs_words[:i+1])
				break
	if not found_prep:
		ingredient.name = right_side
	ingredient.tags, ingredient.substitute = ingredientTagsAndSubs(ingredient)
	return ingredient

# returns true if the prep word is actually part of the ingredient name
def dontIncludeAsPrep(pw, words):
	return (pw in ["shredded", "ground"] and (True in [meat in words for meat in ["beef", "pork", "chicken", "turkey"]]))

# parse the amount needed in decimal
def parse_amount(amount_string):
	if not amount_string:
		return 0

	x = float(amount_string[0:amount_string.find(" ")] if " " in amount_string else 0)
	frac = amount_string[amount_string.find(" ")+1:] if x != 0 else amount_string
	if "/" in amount_string:
		divisor = float(frac[0:frac.find("/")])
		dividend = float(frac[frac.find("/")+1:])
		amt = x + (divisor/dividend)
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
	if i.tags:
		print("Tags: ", i.tags)
	if i.substitute:
		print("Substitutes: ", i.substitute)

	
def ingredientTagsAndSubs(i):
	tags = []
	substitute = { 1: None,
					2: None,
					3: None,
					4: None, 
          5: None,
          6: None}
	longest = Ingredient()
	for category, lst in knowledgebase.categories.items():
		for ingr in lst:
			if contains_word(i.name, ingr.name):
				if len(ingr.name) > len(longest.name):
					longest = ingr
					tags = []
					substitute = { 1: None,
									2: None,
									3: None,
									4: None,
                  5: None,
                  6: None}
				if category not in tags:
					tags.append(category)
					for sub in knowledgebase.substitute_map[category]:
						if ingr.name in knowledgebase.substitute_map[category][sub].canreplace:
							substitute[category] = sub
			elif i.name[-1] == 's':
				if contains_word(i.name, ingr.name+'s'):
					if len(ingr.name) > len(longest.name):
						longest = ingr
						tags = []
						substitute = { 1: None,
										2: None,
										3: None,
										4: None,
                    5: None,
                    6: None}
					if category not in tags:
						tags.append(category)
						for sub in knowledgebase.substitute_map[category]:
							if ingr.name in knowledgebase.substitute_map[category][sub].canreplace:
								substitute[category] = sub

	return tags, {k: v for k, v in substitute.items() if v is not None}


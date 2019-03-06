import validators

# returns a list of the "keywords" found in "strings"
def findWordsInSteps(keywords, strings):
	keywordsfound = []
	for string in strings:
		for keyword in keywords:
			if keyword in string.lower():
				keywordsfound.append(keyword.capitalize())
	return keywordsfound


transformations_display = { 0: "None",
					1: "To vegetarian", # not vegetarian
					2: "To non vegetarian", # vegetarian
					3: "To unhealthy", # healthy
					4: "To healthy", # unhealthy
					5: "To mexican",
					6: "To kosher"
					}

transformations = { 0: "NONE",
					1: "from not vegetarian",
					2: "from vegetarian",
					3: "from unhealthy",
					4: "from healthy", 
					5: "from not mexican",
					6: "from not kosher",
					}

def validatePageLink(err=False):
	if err:
		print("** INVALID URL **\n Please try again.")
	inp = input("Please enter a recipe URL: ")
	page_link = inp if validators.url(inp) else (validatePageLink(True))
	return page_link

def validateTransform(err=False):
	if err:
		print("** INVALID TRANSFORM **\n Please try again.")

	print("\nRecipe Transformations:")
	for k, v in transformations_display.items():
	     print("%d\t%s" % (k, v))
	inp = input("Please enter the number corresponding to the transformation you'd like to perform:\t")
	try:
		transf = int(inp) if int(inp) in transformations.keys() else (validateTransform(True))
	except:
		transf = validateTransform(True) 
	return transf

def contains_word(s, w):
	s = s.lower()
	w = w.lower()
	return (' ' + w + ' ') in (' ' + s + ' ')

def removeDuplicates(recipe):
	new_ingredients = []
	garbage_duplicates = []
	duplicate_indices = []
	original_amounts = {}
	l = len(recipe.ingredients)
	for i in range(0,l):
		ingr_i = recipe.ingredients[i]
		if i in garbage_duplicates:
			continue
		for j in range(0,len(recipe.ingredients)):
			ingr_j = recipe.ingredients[j]
			if not j == i and not j in garbage_duplicates:
				if ingr_i.name == ingr_j.name and (ingr_i.changed or ingr_j.changed):
					if ingr_i.quantity:
						ingr_j.changed = True
						ingr_i.changed = True
						duplicate_indices.append(i)
						garbage_duplicates.append(j)
						if i in original_amounts:
							ingr_i.quantity = ingr_i.quantity + original_amounts[i]
						else:
							original_amounts[i] = ingr_i.quantity
							ingr_i.quantity = ingr_i.quantity * 2
					elif recipe.ingredients[j].quantity:
						ingr_j.changed = True
						ingr_i.changed = True
						duplicate_indices.append(j)
						garbage_duplicates.append(i)
						if j in original_amounts:
							ingr_j.quantity = ingr_j.quantity + original_amounts[j]
						else:
							original_amounts[j] = ingr_j.quantity
							ingr_j.quantity = ingr_j.quantity * 2
	#only add the unique ones
	for i in range(0,l):
		if not i in garbage_duplicates:
			new_ingredients.append(recipe.ingredients[i])
	recipe.ingredients = new_ingredients

	#remove duplicate names in each step
	for step in recipe.steps:
		step.ingredients = list(set(step.ingredients))
	return recipe



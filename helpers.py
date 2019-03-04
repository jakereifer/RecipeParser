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
					}

transformations = { 0: "NONE",
					1: "from not vegetarian",
					2: "from vegetarian",
					3: "from unhealthy",
					4: "from healthy", 
					5: "from not mexican",
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

import validators

# returns a list of the "keywords" found in "strings"
def findWordsInSteps(keywords, strings):
	keywordsfound = []
	for string in strings:
		for keyword in keywords:
			if keyword in string.lower():
				keywordsfound.append(keyword.capitalize())
	return keywordsfound


transformations = { 0: "NONE",
					1: "TO_VEGETARIAN",
					2: "FROM_VEGETARIAN",
					3: "TO_HEALTHY",
					4: "FROM_HEALTHY", 
					5: "TO_CUISINE",
					6: "FROM_CUISINE" }

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
	for k, v in transformations.items():
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

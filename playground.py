from bs4 import BeautifulSoup
import requests

def findWordsInSteps(tools, steps):
	toolsfound = []
	for step in steps:
		for tool in tools:
			if tool in step.lower():
				toolsfound.append(tool.capitalize())
	return toolsfound


tools = ["spoon", "fork", "knife", "oven"]
steps = ["use a fork and spoon", "put it in the oven"]

"""

 Ingredient name
  Quantity
  Measurement (cup, teaspoon, pinch, etc.)
  (optional) Descriptor (e.g. fresh, extra-virgin)
  (optional) Preparation (e.g. finely chopped)
"""

class Ingredient(object):
	name = ""
	quantity = ""
	measurement = ""
	descriptor = ""
	preparation = ""

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
			ingredient.quantity = i_words[0]
			ingredient.name = i_words[1]
			ingredient.measurement = "count"
		return ingredient
	name = 0
	prep_dividers = [",", " - "]
	# last word index
	end = len(i_words)-1
	# Get the quantityquantity
	if i[0].isnumeric():
		ingredient.quantity = i_words[0].strip()
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
		if i_words[1][0].isnumeric():
			ingredient.measurement = " ".join(i_words[1:3]).strip()
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

# Prompt
page_link = input("Please enter a recipe URL: ")
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")

# Scrape for recipe title
recipe_title = page_content.find("h1", {"id": "recipe-main-content"}).text
print("")
print(recipe_title)
print("")

# Scrape for ingredients
scraped_ingredients = [] #
number_of_ingredients = len(page_content.find_all("span", {"class": "recipe-ingred_txt added"}))
for i in range(0, number_of_ingredients):
    ingredient_string = page_content.find_all("span", {"class": "recipe-ingred_txt added"})[i].text
    scraped_ingredients.append(ingredient_string.strip())

# Scrape for steps
scraped_steps = []
number_of_steps = len(page_content.find_all("span", {"class": "recipe-directions__list--item"}))
for i in range(0, number_of_steps):
    step_string = page_content.find_all("span", {"class": "recipe-directions__list--item"})[i].text
    scraped_steps.append(step_string.strip())

for i in scraped_ingredients:
	printIngredient(parseIngredient(i))
	print("")

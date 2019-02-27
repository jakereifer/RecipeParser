from bs4 import BeautifulSoup
import requests
import ingredientparser
import knowledgebase
import helpers
import jakeparser

# test recipe URL: https://www.allrecipes.com/recipe/245863/chicken-stuffed-baked-avocados/?internalSource=popular&referringContentType=Homepage&clickId=cardslot%202
# https://www.allrecipes.com/recipe/10552/giant-chocolate-chip-cookie/?internalSource=hub%20recipe&referringContentType=Search
# with parens: https://www.allrecipes.com/recipe/8350/chantals-new-york-cheesecake/?internalSource=hub%20recipe&referringId=79&referringContentType=Recipe%20Hub&clickId=cardslot%2015

# Prompt for URL
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

#Print parsed ingredients
for i in scraped_ingredients:
	ingredientparser.printIngredient(ingredientparser.parseIngredient(i))
	print("")

# find tools and methods
final_steps = jakeparser.separateIntermediateSteps(scraped_steps)
print(final_steps)

#parse the steps
#separate sentences
#look for duration/ingredients and methods

"""
#Primary methods
primary_methods = set()
for step in scraped_steps:
	primary_methods.update(helpers.findWordsInStep(knowledgebase.primary_methods, step))
print("Primary Methods: ", list(primary_methods))

#Tools

tools = set()
for step in scraped_steps:
	primary_methods.update(helpers.findWordsInStep(knowledgebase.tools, step))
print("Tool: ", list(tools))



#Step by step tools

def checkTransformationSelection(s):
	if s.lower() == 'a':
		return True
	if s.lower() == 'b':
		return True
	if s.lower() == 'c':
		return True
	if s.lower() == 'd':
		return True
	if s.lower() == 'e':
		return True
	return False

valid_transformation = False
transformation_selection = ""
while (!valid_transformation):
	print("")
	print("What type of transformation would you like to make?")
	print("		a - to vegetarian")
	print("		b - from vegetarian")
	print("		c - to healthy")
	print("		d - from healthy")
	print("		e - to style")
	transformation_selection = input("Please input the letter of the choice you would like: ")
	if checkTransformationSelection(transformation_selection):
		valid_transformation = True
	else:
		print("Invalid input")
		print("")

"""




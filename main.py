from bs4 import BeautifulSoup
import requests
import ingredientparser
import re

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

# #Print parsed ingredients
# for i in scraped_ingredients:
# 	ingredientparser.printIngredient(ingredientparser.parseIngredient(i))
# 	print("")



# Step Parsing

stopWords = ['a', 'in', 'the', 'to']
timeMeasures = ['minutes', 'hours', 'seconds']
commonIngredients = ['water']

tempIngredientNames = []
for i in scraped_ingredients:
	parsed = ingredientparser.parseIngredient(i)
	tempIngredientNames.append(parsed.name)

ingredientNames = tempIngredientNames + commonIngredients

# seperate scraped_steps by period
# seperate by semicolon also!
temp = []
for step in scraped_steps:
	temp = temp + step.split('.')

scraped_steps = temp

for step in scraped_steps:
	print("current step: ", step)
	step = re.sub(r'[^\w\s]','',step)
	foundNumber = False
	for word in step.split():
		# find ingredients
		for i in ingredientNames:
			if word in i and not word in stopWords:
				print("Found Ingredient: ", i)
		# do same for method and tools with csvs
		# find times
		if word.isdigit():
			print("found number: ", word)
			foundNumber = True
		for m in timeMeasures:
			if word in m and not word in stopWords:
				print("found time measure: ", m)



		
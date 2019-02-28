from bs4 import BeautifulSoup
import requests
import ingredientparser
import stepparsery
import knowledgebase

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
print("INGREDIENTS")
print("           ")
for i in scraped_ingredients:
	ingredientparser.printIngredient(ingredientparser.parseIngredient(i))
	print("")

print("STEPS")
print("           ")
stepsList = stepparsery.parseSteps(scraped_steps, scraped_ingredients)
stepparsery.printStepInfo(stepsList)


# get list of Tools, Methods (primary and secondary)
scraped_tools = []
scraped_primary_methods = []
scraped_secondary_methods = []
for s in stepsList:
	scraped_tools = scraped_tools + s.tools
	for m in s.methods:
		for p in knowledgebase.primary_methods:
			if m == p:
				scraped_primary_methods.append(m)
		for s in knowledgebase.secondary_methods:
			if m == s:
				scraped_secondary_methods.append(m)

print ("ALL FOUND TOOLS")
print("           ")
print(scraped_tools)
print("             ")
print ("ALL FOUND PRIMARY METHODS")
print("           ")
print(scraped_primary_methods)
print("           ")
print ("ALL SECONDARY METHODS")
print("           ")
print(scraped_secondary_methods)



		
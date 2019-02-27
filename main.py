from bs4 import BeautifulSoup
import requests
import ingredientparser
import re
import stepparsery
import jakeparser

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

final_steps=jakeparser.separateIntermediateSteps(scraped_steps)
# print("fs: ", final_steps)
scraped_steps=final_steps

class Step(object):
	def __init__(self):
		self.text = ""
		self.ingList = []
		self.time = ""
		self.methods = []
		self.tools = []

# Step Parsing

commonIngredients = ['water']

ingredientNames = []
for i in scraped_ingredients:
	parsed = ingredientparser.parseIngredient(i)
	ingredientNames.append(parsed.name)

# update this!
for i in commonIngredients:
	if not i in ingredientNames:
		ingredientNames.append(i)

# seperate scraped_steps by period
# seperate by semicolon also!
temp = []
for step in scraped_steps:
	temp = temp + step.split('.')

scraped_steps = temp

stepsDic= {}


for step in scraped_steps:
	if step == "":
		continue
	step = re.sub(r'[^\w\s]','',step)
	stepsDic[step] = Step()

	# Find ingredients
	stepsDic[step].ingList = stepparsery.findIngredients(step, ingredientNames)

	# find times
	stepsDic[step].time = stepparsery.findTimes(step)
	stepsDic[step].methods = stepparsery.findMethods(step)
	stepsDic[step].tools = stepparsery.findTools(step)



stepparsery.printStepInfo(stepsDic)

			



		
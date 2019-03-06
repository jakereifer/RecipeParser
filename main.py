from bs4 import BeautifulSoup
import requests
from ingredientparser import *
from IngredientClass import *
from StepClass import *
from helpers import *
from RecipeClass import *
import knowledgebase
from transform import *


# test recipe URL: https://www.allrecipes.com/recipe/245863/chicken-stuffed-baked-avocados/?internalSource=popular&referringContentType=Homepage&clickId=cardslot%202
# https://www.allrecipes.com/recipe/10552/giant-chocolate-chip-cookie/?internalSource=hub%20recipe&referringContentType=Search
# with parens: https://www.allrecipes.com/recipe/8350/chantals-new-york-cheesecake/?internalSource=hub%20recipe&referringId=79&referringContentType=Recipe%20Hub&clickId=cardslot%2015



# Prompt for URL
recipe = Recipe()
page_link = validatePageLink()


transform_input = validateTransform()
transformation = int(transform_input)
print(transformation, transformations_display[transformation])
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")

# Scrape for recipe title
recipe.name = page_content.find("h1", {"id": "recipe-main-content"}).text
# print("")
# print(recipe.name)
# print("")
servings = page_content.find("meta",{"id": "metaRecipeServings"})["content"]


# number_of_ingredients = len(page_content.find_all("span", {"class": "recipe-ingred_txt added"}))
# for i in range(0, number_of_ingredients):
#     ingredient_string = page_content.find_all("span", {"class": "recipe-ingred_txt added"})[i].text
    # recipe.ingredients.append(IngredientClass.parseIngredient(ingredient_string.strip()))

# Scrape for ingredients
for ingr in page_content.find_all("span", {"class": "recipe-ingred_txt added"}):
	recipe.ingredients.append(parseIngredient(ingr.text.strip()))

#Print parsed ingredients
# print("Ingredients:\n")
# # recipe.ingredients = [IngredientClass.parseIngredient(i) for i in scraped_ingredients]
# for ingr in recipe.ingredients:
# 	ingr.printIngredient()
# 	print("")

# Scrape for steps
scraped_steps = []
number_of_steps = len(page_content.find_all("span", {"class": "recipe-directions__list--item"}))
for i in range(0, number_of_steps):
    step_string = page_content.find_all("span", {"class": "recipe-directions__list--item"})[i].text
    scraped_steps.append(step_string.strip())

scraped_ingredients = [i.text.strip() for i in page_content.find_all("span", {"class": "recipe-ingred_txt added"})]
# print("STEPS")
# print("           ")

recipe.steps = parseSteps(scraped_steps, scraped_ingredients)

recipe.tools = list(set([tool for s in recipe.steps for tool in s.tools if tool not in recipe.tools]))
recipe.p_methods = list(set([method for s in recipe.steps for method in s.methods if method in knowledgebase.primary_methods and method not in recipe.p_methods]))
recipe.s_methods = list(set([method for s in recipe.steps for method in s.methods if method in knowledgebase.secondary_methods and method not in recipe.s_methods]))

recipe.sortIngredientsIntoCategories() 
# recipe.printRecipe()


if transformation != 0:
	print("_____________________________________")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("After Transformation")
	print("")
	recipe = TransformRecipe(recipe,transformation, servings)
	recipe.printRecipe()

# get list of Tools, Methods (primary and secondary)
# scraped_tools = []
# scraped_primary_methods = []
# scraped_secondary_methods = []
# for s in stepsList:
# 	scraped_tools = scraped_tools + s.tools
# 	for m in s.methods:
# 		for p in knowledgebase.primary_methods:
# 			if m == p:
# 				scraped_primary_methods.append(m)
# 		for s in knowledgebase.secondary_methods:
# 			if m == s:
# 				scraped_secondary_methods.append(m)

# print ("ALL FOUND TOOLS")
# print("           ")
# print(recipe.tools)
# print("             ")
# print ("ALL FOUND PRIMARY METHODS")
# print("           ")
# print(recipe.p_methods)
# print("           ")
# print ("ALL SECONDARY METHODS")
# print("           ")
# print(recipe.s_methods)


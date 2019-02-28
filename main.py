from bs4 import BeautifulSoup
import requests
import ingredientparser
import knowledgebase
from helpers import *



# test recipe URL: https://www.allrecipes.com/recipe/245863/chicken-stuffed-baked-avocados/?internalSource=popular&referringContentType=Homepage&clickId=cardslot%202
# https://www.allrecipes.com/recipe/10552/giant-chocolate-chip-cookie/?internalSource=hub%20recipe&referringContentType=Search
# with parens: https://www.allrecipes.com/recipe/8350/chantals-new-york-cheesecake/?internalSource=hub%20recipe&referringId=79&referringContentType=Recipe%20Hub&clickId=cardslot%2015



# Prompt for URL
recipe = Recipe()
page_link = validatePageLink()


transform_input = validateTransform()
transformation = transformations[int(transform_input)]
print(transformation)
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")

# Scrape for recipe title
recipe.name = page_content.find("h1", {"id": "recipe-main-content"}).text
print("")
print(recipe.name)
print("")


# number_of_ingredients = len(page_content.find_all("span", {"class": "recipe-ingred_txt added"}))
# for i in range(0, number_of_ingredients):
#     ingredient_string = page_content.find_all("span", {"class": "recipe-ingred_txt added"})[i].text
    # recipe.ingredients.append(ingredientparser.parseIngredient(ingredient_string.strip()))

# Scrape for ingredients
for ingr in page_content.find_all("span", {"class": "recipe-ingred_txt added"}):
	recipe.ingredients.append(ingredientparser.parseIngredient(ingr.text.strip()))
#Print parsed ingredients
print("Ingredients:\n")
# recipe.ingredients = [ingredientparser.parseIngredient(i) for i in scraped_ingredients]
for ingr in recipe.ingredients:
	ingredientparser.printIngredient(ingr)
	print("")

# Scrape for steps
scraped_steps = []
number_of_steps = len(page_content.find_all("span", {"class": "recipe-directions__list--item"}))
for i in range(0, number_of_steps):
    step_string = page_content.find_all("span", {"class": "recipe-directions__list--item"})[i].text
    recipe.steps.append(step_string.strip())



# find tools and methods


#parse the steps
#separate sentences
#look for duration/ingredients and methods
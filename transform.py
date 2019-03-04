from RecipeClass import *
from knowledgebase import *


def TransformRecipe(recipe, transform, servings):
	new_ingr = recipe.ingredients
	# grab ingredients to change
	bad_ingredients = recipe.categories[transform]
	#find substitutes
	subs = {}
	for bad_ingredient in bad_ingredients:
		subs[bad_ingredient.name] = bad_ingredient.substitute[transform]
	for step in recipe.steps:
		for i in range(0,len(step.ingredients)):
			for bad_ingredient in bad_ingredients:
				if step.ingredients[i] == bad_ingredient.name:
					step.ingredients[i] = subs[bad_ingredient.name]

	# Quantity and ingredient
	replacement_dict = substitute_map[transform] 
	for ingredient in recipe.ingredients:
		for k in subs:
			if k == ingredient.name:
				ingredient.name = subs[k]
				ingredient.preparation = ""
				subs_ingr = replacement_dict[subs[k]]
				print(subs_ingr.quantity)
				if not ingredient.measurement or not ingredient.measurement in subs_ingr.quantity:
					ingredient.measurement = subs_ingr.quantity["default"][1]
					ingredient.quantity = float(subs_ingr.quantity["default"][0]) * float(servings)
				else:
					ingredient.measurement = subs_ingr.quantity[ingredient.measurement][1]
					ingredient.quantity = float(ingredient.quantity) * float(subs_ingr.quantity[ingredient.measurement][0])
				# quantity









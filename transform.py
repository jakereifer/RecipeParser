from RecipeClass import *
def TransformRecipe(recipe, transform_rules, transform):
	new_ingr = recipe.ingredients
	# grab ingredients to change
	bad_ingredients = recipe.categories[1]
	#find substitutes
	subs = {}
	for bad_ingredient in bad_ingredients:
		subs[bad_ingredient.name] = bad_ingredient.substitute[1]
	for step in recipe.steps:
		for i in range(0,len(step.ingredients)):
			for bad_ingredient in bad_ingredients:
				if step.ingredients[i] == bad_ingredient.name:
					step.ingredients[i] = subs[bad_ingredient.name]

	# Quantity and ingredient
	for ingredient in recipe.ingredients:
		for k in subs:
			if k == ingredient.name:
				ingredient.name = subs[k]
				ingredient.preparation = ""







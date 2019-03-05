from RecipeClass import *
from knowledgebase import *
from helpers import *
from ingredientparser import *

def TransformRecipe(recipe, transform, servings):
	# grab ingredients to change
	bad_ingredients = recipe.categories[transform]
	#find substitutes
	made_sub = False
	subs = {}
	for bad_ingredient in bad_ingredients:
		# print("BAD INGR NAME ", bad_ingredient.name)
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
				made_sub = True
				ingredient.name = subs[k]
				ingredient.changed = True
				ingredient.preparation = ""
				subs_ingr = replacement_dict[subs[k]]
				# print(subs_ingr.quantity)
				if not ingredient.measurement or not ingredient.measurement in subs_ingr.quantity:
					ingredient.measurement = subs_ingr.quantity["default"][1]
					ingredient.quantity = float(subs_ingr.quantity["default"][0]) * float(servings)
				else:
					ingredient.measurement = subs_ingr.quantity[ingredient.measurement][1]
					ingredient.quantity = float(ingredient.quantity) * float(subs_ingr.quantity[ingredient.measurement][0])
				# quantity

	#for mexican
	pre_mex_seasonings = ["chili powder", "garlic powder", "cumin", "onion powder", "paprika", "oregano", "red pepper flakes"]
	mex_seasonings = []
	for seasoning in pre_mex_seasonings:
		found = False
		for ingredient in recipe.ingredients:
			if contains_word(ingredient.name, seasoning):
				found = True
		if not found:
			mex_seasonings.append(seasoning)
	if transform == 5:
		for ingredient in recipe.ingredients:
			# if ingredient.tags:
			# print("Ingr: ", ingredient.name, "tags: ", ingredient.tags)
			if "seasoning" in ingredient.tags:
				if len(mex_seasonings) > 0:
					ingredient.name = mex_seasonings.pop(0)
					if not ingredient.measurement:
						ingredient.measurement = "teaspoon"
						ingredient.quantity = parse_amount("1")
		new_ingredients = []
		while len(mex_seasonings) > 0:
			new_ingr = Ingredient(mex_seasonings.pop(0), parse_amount("1"), "teaspoon", "","",[],{ 1: "", 2: "", 3: "",4: "", 5: ""})
			new_ingredients.append(new_ingr)
		if not new_ingredients == []: 
			recipe.ingredients = recipe.ingredients + new_ingredients
			s = Step()
			s.text = "sprinkle seasoning on top of dish"
			s.ingredients = [new_ingr.name for new_ingr in new_ingredients]
			s.time = ""
			s.methods = ["sprinkle"]
			s.tools = []
			recipe.steps.append(s)
	#for unhealthy
	if transform == 3 and not made_sub:
		#bacon
		bacon = Ingredient("bacon strips",float(servings) * 2, "","","",[],{ 1: "", 2: "", 3: "",4: "", 5: ""})
		#powedered sugar
		sugar = Ingredient("powdered sugar",float(servings) * 1, "teaspoon", "", "", [], { 1: "", 2: "", 3: "",4: "", 5: ""})
		recipe.ingredients = recipe.ingredients + [bacon,sugar]
		#creating the steps 
		cookBacon = Step()
		cookBacon.text = "cook bacon on pan for fifteen minutes"
		cookBacon.ingredients = [bacon.name]
		cookBacon.time = "fifteen minutes"
		cookBacon.methods = ["cook"]
		cookBacon.tools = ["pan"]
		recipe.steps.append(cookBacon)

		sliceBacon = Step()
		sliceBacon.text = "slice bacon into bits"
		sliceBacon.ingredients = [bacon.name]
		sliceBacon.time = ""
		sliceBacon.methods = ["slice"]
		sliceBacon.tools = ["knife"]
		recipe.steps.append(sliceBacon)

		spreadUnhealthy = Step()
		spreadUnhealthy.text = "generously sprinkle bacon bits and powdered sugar over dish"
		spreadUnhealthy.ingredients = [bacon.name, sugar.name]
		spreadUnhealthy.time = ""
		spreadUnhealthy.methods = ["sprinkle"]
		spreadUnhealthy.tools = []
		
		#adding the steps to the recipe
		recipe.steps.append(spreadUnhealthy)

	removeDuplicates(recipe)
		










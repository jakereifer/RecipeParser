import knowledgebase

for i in knowledgebase.ingredients_kb:
	missingTags = []
	for t in i.tags:
		foundRep = False 
		curr_map = knowledgebase.substitute_map[t]
		for sub in curr_map:
			for rep in curr_map[sub].canreplace:
				if i.name.lower() == rep.lower():
					foundRep = True
		if foundRep == False:
			missingTags.append(t)
	if len(missingTags)>0:
		print("Ingredient: ", i.name)
		print("Missing in tags: ", missingTags)
		print("              ")

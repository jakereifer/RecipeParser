def findTimes(step):
	foundNumber = False
	foundRange = False
	foundRelativeTime = False
	foundOr = False
	time = ""
	timeMeasures = ['minutes', 'hours', 'seconds']
	for word in step.split():
		if foundNumber:
				if word == 'to':
					time = time + ' '+ word
					# print("adding to: ", stepsDic[step].time)
				elif word in timeMeasures:
					time = time + ' '+ word
					foundNumber = False
					# print("adding measure: ", stepsDic[step].time)
				elif word.isdigit():
					time = time + ' '+ word
					# print("adding digit: ", stepsDic[step].time)			
				else: 
					# print("confounding digit found")
					time = ""
					foundNumber = False
		else:
			if word.isdigit():
				foundNumber = True
				time = word
				# print("found first number: ", stepsDic[step].time
		if foundRelativeTime:
			time = time + ' ' + word
		else:
			if word == 'until':
				foundRelativeTime = True
				time = word

	return time

def findIngredients(step, ingredientNames):
	# stepIngredients = []
	# for i in ingredientNames:
	# 	if contains_word(step, i) and not i in stepIngredients:
	# 		stepIngredients.append(i)
	# return stepIngredients

	stopWords = ['on', 'in', 'to', 'from']
	finalIngs = []
	words = step.split()
	for a in range(len(words)):
		tempIng = []
		for i in ingredientNames:
			if words[a] in i and not words[a] in stopWords:
				tempIng.append(i)
		if len(tempIng) > 1:
			if a == len(words) - 1:
				finalIngs = finalIngs + tempIng
			else:
				longerWord = words[a]
				for b in range(a, len(words)-1):
			 		longerWord = longerWord + ' ' + words[b+1]
		 			newTempIng = []
		 			for z in tempIng:
		 				if longerWord in z:
		 					newTempIng.append(z)
		 			tempIng = newTempIng
		 			if not len(tempIng) > 1: 
		 				a = b + 2
		 				finalIngs = finalIngs + tempIng
		 				break		 			

		else:
			finalIngs = finalIngs + tempIng
	finalIngs = list(set(finalIngs))
	return finalIngs






def printStepInfo(stepsDic):
	for s in stepsDic:
		print("step: ", s)
		print("ingredients: ", stepsDic[s].ingList)
		print("time: ", stepsDic[s].time)
		print("            ")

def contains_word(s, w):
    return (' ' + w + ' ') in (' ' + s + ' ')

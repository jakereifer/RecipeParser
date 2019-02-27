import knowledgebase
import helpers


def findTimes(step):
	foundNumber = False
	foundRange = False
	foundRelativeTime = False
	foundOr = False
	time = ""
	timeMeasures = ['minutes', 'hours', 'seconds', 'hour', 'minute', 'second']
	for word in step.split():
		if foundNumber:
				if word == 'to':
					time = time + ' '+ word
					# print("adding to: ", stepsDic[step].time)
				elif word.lower() in timeMeasures:
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


def findMethods(step):
	finalMethods = []
	methodList = knowledgebase.primary_methods + knowledgebase.secondary_methods
	for method in methodList:
		if contains_word(step, method) and not method in finalMethods:
			finalMethods.append(method)
	return finalMethods



	# methodList = knowledgebase.primary_methods + knowledgebase.secondary_methods
	# return helpers.findWordsInSteps(methodList, [step])

def findIngredients(step, ingredientNames):
	return findKeywords(step, ingredientNames)
	# stopWords = ['on', 'in', 'to', 'from']
	# finalIngs = []
	# words = step.split()
	# for a in range(len(words)):
	# 	tempIng = []
	# 	for i in ingredientNames:
	# 		if words[a] in i and not words[a] in stopWords:
	# 			tempIng.append(i)
	# 	if len(tempIng) > 1:
	# 		if a == len(words) - 1:
	# 			finalIngs = finalIngs + tempIng
	# 		else:
	# 			longerWord = words[a]
	# 			for b in range(a, len(words)-1):
	# 		 		longerWord = longerWord + ' ' + words[b+1]
	# 	 			newTempIng = []
	# 	 			for z in tempIng:
	# 	 				if longerWord in z:
	# 	 					newTempIng.append(z)
	# 	 			tempIng = newTempIng
	# 	 			if not len(tempIng) > 1: 
	# 	 				a = b + 2
	# 	 				finalIngs = finalIngs + tempIng
	# 	 				break		 			
	# 	else:
	# 		finalIngs = finalIngs + tempIng
	# finalIngs = list(set(finalIngsq))
	# return finalIngs

# def findKeywords(step, listWords):
# 	stopWords = ['on', 'in', 'to', 'from', 'for', 'al']
# 	finalIngs = []
# 	words = step.split()
# 	for a in range(len(words)):
# 		tempIng = []
# 		for i in listWords:
# 			if words[a] in i and not words[a] in stopWords:
# 				tempIng.append(i)
# 		if len(tempIng) > 1:			
# 			if a == len(words) - 1:
# 				finalIngs = finalIngs + tempIng
# 			elif tempIng[0] == tempIng[1]:
# 				finalIngs = finalIngs + [tempIng[0]]
# 			else:
# 				longerWord = words[a]
# 				for b in range(a, len(words)-1):
# 			 		longerWord = longerWord + ' ' + words[b+1]
# 		 			newTempIng = []
# 		 			for z in tempIng:
# 		 				if longerWord in z:
# 		 					newTempIng.append(z)
# 		 			tempIng = newTempIng
# 		 			if not len(tempIng) > 1: 
# 		 				a = b + 2
# 		 				finalIngs = finalIngs + tempIng
# 		 				break		 			
# 		else:
# 			finalIngs = finalIngs + tempIng
# 	finalIngs = list(set(finalIngs))
# 	return finalIngs

def findKeywords(step, listWords):
	stopWords = ['on', 'in', 'to', 'from', 'for', 'al', 'at', 'a']
	finalIngs = []
	words = step.split()
	for a in range(len(words)):
		tempIng = []
		direct = ""
		for i in listWords:
			if words[a] in i and not words[a] in stopWords:
				tempIng.append(i)
				if 'water' in tempIng:
					print("1: ", words[a])
				if words[a].lower() == i.lower():
					direct=i
		tempIng = list(set(tempIng))
		if len(tempIng) > 1:
			# end of string check
			if a == len(words) - 1:
				if not direct =="":
					if direct == "water":
						print("3")
					finalIngs.append(direct)				
				else:
					finalIngs = finalIngs + tempIng
			else:
				longerWord = words[a]
				for b in range(a, len(words)-1):
			 		longerWord = longerWord + ' ' + words[b+1]
		 			newTempIng = []
		 			for z in tempIng:
		 				if longerWord in z:
		 					newTempIng.append(z)
		 					if longerWord == z.lower():
		 						direct=i 
		 			tempIng = newTempIng
		 			if 'water' in tempIng:
		 				print("2")
		 			if tempIng == []: 
		 				a = b + 1
		 				if not direct =="":
		 					finalIngs.append(direct)
		 				break		 			
		else:
			finalIngs = finalIngs + tempIng
	finalIngs = list(set(finalIngs))
	return finalIngs



def findTools(step):
	finalList = []
	toolList = knowledgebase.tools
	for tool in toolList:
		if contains_word(step, tool) and not tool in finalList:
			finalList.append(tool)
	return finalList
	# toolList = knowledgebase.tools
	# return findKeywords(step, toolList)
	# finalList = []
	# toolList = knowledgebase.tools
	# words = step.split()
	# for word in words:
	# 	for tool in toolList:
	# 		if contains_word(tool, word) and not tool in finalList:
	# 			finalList.append(tool)
	# return finalList


	# toolList = knowledgebase.tools
	# return helpers.findWordsInSteps(toolList, [step])



def printStepInfo(stepsDic):
	for s in stepsDic:
		print("step: ", s)
		print("ingredients: ", stepsDic[s].ingList)
		print("time: ", stepsDic[s].time)
		print("methods: ", stepsDic[s].methods)
		print("tools: ", stepsDic[s].tools)
		print("            ")

def contains_word(s, w):
	s = s.lower()
	w = w.lower()
	return (' ' + w + ' ') in (' ' + s + ' ')

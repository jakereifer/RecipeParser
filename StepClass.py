import knowledgebase
import helpers
from nltk.corpus import stopwords
import IngredientClass
import ingredientparser
import RecipeClass
import jakeparser
import re

sw = stopwords.words("english")


class Step(object):
	def __init__(self):
		self.text = ""
		self.ingredients = []
		self.time = ""
		self.methods = []
		self.tools = []


def parseSteps(scraped_steps, scraped_ingredients):
	# create Dictionary
	stepsList = []
	# clean ingredients
	ingredientNames = cleanIngredients(scraped_ingredients)
	# clean steps
	cleaned_steps = jakeparser.separateIntermediateSteps(scraped_steps)
	# loop through steps
	for step in cleaned_steps:
		# clean tweet
		if step == "":
			continue
		currStep = Step()
		currStep.text = step
		cleanStep = re.sub(r'[^\w\s]','',step)
		# run each function
		currStep.ingredients = findIngredients(cleanStep, ingredientNames)
		currStep.time = findTimes(cleanStep)
		currStep.methods = findMethods(cleanStep)
		currStep.tools = findTools(cleanStep)
		stepsList.append(currStep)

		
	# return Dictionary
	return stepsList

def cleanIngredients(scraped_ingredients):
	commonIngredients = ['water']
	ingredientNames = []
	for i in scraped_ingredients:
		parsed = ingredientparser.parseIngredient(i)
		ingredientNames.append(parsed.name)
	for i in commonIngredients:
		if not i in ingredientNames:
			ingredientNames.append(i)
	return ingredientNames


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
					# print("add to: ", time)
				elif word.lower() in timeMeasures:
					time = time + ' '+ word
					foundNumber = False
					# print("adding measure: ", time)
					# print("adding measure: ", stepsDic[step].time)
				elif word.isdigit():
					time = time + ' '+ word
					# print("adding another digit: ", time)
					# print("adding digit: ", stepsDic[step].time)			
				else: 
					# print("confounding digit found")
					# print("confounding")
					time = ""
					foundNumber = False
		else:
			if word.isdigit():
				foundNumber = True
				foundRelativeTime = False
				time = word
				# print("found first digit: ", time)
		if foundRelativeTime:
			time = time + ' ' + word
			# print("found after until: ", time)
		else:
			if word == 'until':
				foundRelativeTime = True
				foundNumber = False
				time = word
				# print("found until: ", time)
	return time


def findMethods(step):
	finalMethods = []
	methodList = knowledgebase.primary_methods + knowledgebase.secondary_methods
	for method in methodList:
		if contains_word(step, method) and not method in finalMethods:
			finalMethods.append(method)
	return finalMethods


def findIngredients(step, ingredientNames):
	return findKeywords(step, ingredientNames)


def findKeywords(step, listWords):
	# stopWords = ['on', 'in', 'to', 'from', 'for', 'al', 'at', 'a', 'so', 'it']
	finalIngs = []
	words = step.split()
	for a in range(len(words)):
		tempIng = []
		direct = ""
		for i in listWords:
			if words[a] in i and not words[a] in sw:
				tempIng.append(i)
				if words[a].lower() == i.lower():
					direct=i
		tempIng = list(set(tempIng))
		if len(tempIng) > 1:
			# end of string check
			if a == len(words) - 1:
				if not direct =="":
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
		 						direct=z 
		 			tempIng = newTempIng
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



def printStepInfo(stepsList):
	for s in stepsList:
		print("step: ", s.text)
		print("ingredients: ", s.ingredients)
		print("time: ", s.time)
		print("methods: ", s.methods)
		print("tools: ", s.tools)
		print("            ")

def contains_word(s, w):
	s = s.lower()
	w = w.lower()
	return (' ' + w + ' ') in (' ' + s + ' ')

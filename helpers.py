import knowledgebase
import helpers

# returns a list of the "keywords" found in "strings"
def findWordsInStep(keywords, string):
	keywordsfound = []
	print(string.lower())
	for keyword in keywords:
		print(keyword)
		if keyword.lower() in string.lower():
			print("FOUND!!!!")
			keywordsfound.append(keyword.capitalize())
	return keywordsfound


def addsTools(string):
	m = list(set(helpers.findWordsInSteps(primary_methods, string)))
	final_tools = set(helpers.findWordsInSteps(tools, string))
	for element in m:
		if element in knowledgebase.method_tools.keys():
			final_tools.update(knowledgebase.method_tools[element])
	return list(final_tools)
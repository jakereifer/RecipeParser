import spacy
import knowledgebase
# multiple things in one sentence
# finding tools and 


# def parseStep(step):
# 	step = Step()
# 	steptime = findTime()
# 	method = findMethod()
# 	tools = findTools()

def separateIntoClauses(sentence):
	sentence = sentence.strip()
	clauses = []
	if sentence == "":
		return [""]
	nlp = spacy.load('en_core_web_sm')
	doc = nlp(sentence)
	verbs = []
	first_verb = False
	temp_clause = []
	check_kb = False
	until = False
	prev_doc_token = ""
	after_comma = False
	for i in range(0,len(doc)):
		if prev_doc_token == ",":
			after_comma = True
		else:
			after_comma = False
		prev_doc_token = doc[i].text
		if doc[i].text.lower() == "until":
			until = True
			check_kb = True
		if doc[i].pos_ == "VERB" and not badWords(doc[i].text.lower(), doc[i].lemma_) and after_comma:
			if until:
				until = False
				continue
			check_kb = True
			# print(token, token.pos_)
			if not first_verb:
				first_verb = True
			else:
				if not i == 0 and not doc[i-1].text == "to" and not "does" in doc[i-1].text and after_comma:
					clauses.append(sentence.split(str(doc[i]))[0])
					# print("CLAUSES", clauses)
					sentence = str(doc[i]) + " ".join(sentence.split(str(doc[i]))[1:])
					# print("SENTENCE", clauses)
		else:
			if not check_kb:
				if str(doc[i]).strip().lower() in knowledgebase.primary_methods or str(doc[i]).strip().lower() in knowledgebase.secondary_methods:
					# print(token, token.pos_)
					first_verb = True
					check_kb = True
	clauses.append(sentence)
	return clauses



def badWords(word, lemma):
	if word == "oven":
		return True
	if word == "seasoned":
		return True
	if word == "seasoning":
		return True
	if word == "should":
		return True
	if word == "preheated":
		return True
	if word == "continue":
		return True
	if lemma == "be":
		return True
	if lemma == "do":
		return True
	for prep_word in knowledgebase.preparations:
		if word == prep_word:
			return True
	return False


def splitBySentence(s):
	return s.replace(";",".").split(".")


def separateIntermediateSteps(steps):
	temp_steps = []
	final_steps = []
	returned_steps = []
	last_steps = []
	for step in steps:
		temp_steps = temp_steps + splitBySentence(step)
	for temp_step in temp_steps:
		final_steps = final_steps + separateIntoClauses(temp_step)
	for final_step in final_steps:
		if not final_step.strip() == "":
			returned_steps.append(final_step.strip())
	skip = False
	for i in range(0,len(returned_steps)):
		returned_steps[i] = returned_steps[i].strip()
		# print(returned_steps[i])
		if len(returned_steps[i]) < 1:
			skip = True
		if skip:
			skip = False
			continue
		if len(returned_steps[i].strip().split()) == 1:
			if i+1 < len(returned_steps):
				last_steps.append(" ".join([returned_steps[i],returned_steps[i+1]]))
				skip = True
		else:
			last_steps.append(returned_steps[i])
	return last_steps




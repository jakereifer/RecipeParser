from nltk.corpus import stopwords
sw = stopwords.words("english")
def findKeywords(step, listWords):
	# stopWords = ['on', 'in', 'to', 'from', 'for', 'al', 'at', 'a', 'so', 'it']
	finalIngs = []
	words = step.split()
	for word in words:
		word = word.lower()
	for lw in listWords:
		lw = lw.lower()
	i_locs = {}
	l = len(words)
	a = 1
	while a < l:
		# print("a: ",a, "words[a]: ", words[a])
		tempIng = []
		direct = ""
		for i in listWords:
			if words[a].lower() in i.lower() and not words[a].lower() in sw:
				tempIng.append(i.lower())
				if words[a].lower() == i.lower():
					direct=i
		tempIng = list(set(tempIng))
		# print("tempIng: ", tempIng)
		if len(tempIng) > 1:
			# end of string check
			if a == len(words) - 1:
				if not direct =="":
					finalIngs.append(direct)
					if direct in i_locs:
						i_locs[direct].append((a,a))
					else:
						i_locs[direct] = [(a,a)]		
				else:
					finalIngs = finalIngs + tempIng
					for ti in tempIng:
						if ti in i_locs:
							i_locs[ti].append((a,a))
						else:
							i_locs[ti] = [(a,a)]
			else:
				longerWord = words[a].lower()
				for b in range(a, len(words)-1):
					# print("b: ",b)
					longerWord = longerWord + ' ' + words[b+1].lower()
					newTempIng = []
					for z in tempIng:
						if longerWord in z.lower():
							newTempIng.append(z)
							if longerWord == z.lower():
								direct=z 
					tempIng = newTempIng
					if tempIng == []: 
						if not direct =="":
							finalIngs.append(direct)
							if direct in i_locs:
								i_locs[direct].append((a,b))
							else:
								i_locs[direct] = [(a,b)]	
							a = b
						break		 			
		else:
			if len(tempIng) == 1:
				curr = tempIng[0]
				# print("tempIng[0]", tempIng[0])
				finalIngs = finalIngs + tempIng
				end = a
				longer = words[a].lower()
				while end < len(words)-1:
					# print("end", end)
					longer = longer + ' ' + words[end+1].lower()
					if not longer in curr:
						break
					else:
						end = end+1
				if curr in i_locs:
					i_locs[curr].append((a,end))
				else:
					i_locs[curr] = [(a,end)]
				a = end
		a = a + 1
	finalIngs = list(set(finalIngs))
	# print("Step: ",step)
	# print("finalIngs: ", finalIngs)
	# print("i_locs: ", i_locs)
	# print("step: ", step)
	# print("i_locs: ", i_locs)
	return finalIngs, i_locs

findKeywords("Season with sugar chili powder fennel seeds Italian seasoning 1 tablespoon salt pepper and 2 tablespoons parsley", ["Italian Seasoning", "Fennel seeds"])









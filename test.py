from nltk.corpus import stopwords
sw = stopwords.words("english")
def findKeywords(step, listWords):
	# stopWords = ['on', 'in', 'to', 'from', 'for', 'al', 'at', 'a', 'so', 'it']
	finalIngs = []
	words = step.split()
	i_locs = {}
	l = len(words)
	a = 0
	while a < l:
		print("a: ",a)
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
				longerWord = words[a]
				for b in range(a, len(words)-1):
					print("b: ",b)
					longerWord = longerWord + ' ' + words[b+1]
					newTempIng = []
					for z in tempIng:
						if longerWord in z:
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
				print("tempIng[0]", tempIng[0])
				finalIngs = finalIngs + tempIng
				end = a
				longer = words[a]
				while end < len(words)-1:
					print("end", end)
					longer = longer + ' ' + words[end+1]
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
	print("Step: ",step)
	print("finalIngs: ", finalIngs)
	print("i_locs: ", i_locs)
	return finalIngs

findKeywords("Cook lasagna noodles in boiling water for 8 to 10 minutes", ["lasagna noodles", "water"])
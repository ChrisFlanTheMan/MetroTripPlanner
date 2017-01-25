paths = []

fname = "transitMap.txt"
with open(fname) as f:
    content = f.readlines()
    for line in content:
    	info = line.split(', ')
    	for item in info:
    		item.strip()
    	paths.append([info[0], info[1], info[2], info[3], float(info[4])])

start = raw_input()
finish = raw_input()

results = []

optionNum = 0

def printOption(time, firstPathColour, changedStation, secondPathColour):
	global optionNum
	print "Option " + str(optionNum) + " (" + str(round(time, 1)) + "mn) :",
	optionNum += 1
	print "At " + start + ",", 
	print "take " + firstPathColour + " line,",
	if (firstPathColour != ""):
		print "change at " + changedStation,
		print "and take " + secondPathColour + " line",
	print "exit at " + finish		

def next_path(currentStation, currentLineColour, lastPath, changed, changedLineColour, changedStation, time):
	if currentStation == finish:
		if changed == False:
			results.append([time, "", '', lastPath[1]])
		else:
			results.append([time, changedLineColour, changedStation, lastPath[1]])

	for nextPath in paths:
		if (nextPath[0] == currentStation or nextPath[2] == currentStation) and nextPath != lastPath:
			newTime = time + nextPath[4]
			if nextPath[0] == nextPath[2] and changed == False and (currentLineColour == nextPath[1] or currentLineColour == nextPath[3]):
				nextLineColour = nextPath[1] if nextPath[1] != lastPath[1] else nextPath[3]
				next_path(currentStation, nextLineColour, nextPath, True, lastPath[1], currentStation, newTime)
			elif nextPath[0] != nextPath[2] and currentLineColour == nextPath[1]:
				nextStation = nextPath[0] if nextPath[2] == currentStation else nextPath[2]
				next_path(nextStation, currentLineColour, nextPath, changed, changedLineColour, changedStation, newTime)

for path in paths:
	if path[0] == start and path[2] != start:
		next_path(path[2], path[1], path, False, "", '', path[4])

results.sort(key = lambda x: int(x[0]))
for result in results:
	printOption(result[0], result[1], result[2], result[3])




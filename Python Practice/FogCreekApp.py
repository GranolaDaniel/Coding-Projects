import string, operator

SearchString = []
SearchDict = dict()

#Add all values of the search string to a list
for i in string.ascii_lowercase:
	SearchString.append(i)
SearchString.append('_')

#Dictionary for tracking character count
for j in SearchString:
	SearchDict[j] = 0

#Looks at each character in the text and adds all instances to the dictionary
with open('FogCreek.txt') as f:
	FogCreekText = f.read()

	for i in FogCreekText:
		if i in SearchString:
			SearchDict[i] += 1

#Sorted list of characters in descencing order
sorted_values = sorted(SearchDict.items(), key=operator.itemgetter(1), reverse=True)
SecretWord = ''

for l in sorted_values:
	if l[0] == '_':
		break
	else:
		SecretWord += l[0]

print(SecretWord)

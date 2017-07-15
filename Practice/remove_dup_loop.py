from random import randint

#Random list function
def randList():
	num = int(input('Give me the length of this list '))
	ran = []
	
	while len(ran) < num:
		x = randint(0,15)

		ran.append(x)
	return ran

def listRem():
	ranListA = randList()
	ranListB = randList()
	endList = []

	for i in ranListA:
		if i in ranListB:
			endList.append(i)

	print("Your new list is " + str(endList))

listRem()
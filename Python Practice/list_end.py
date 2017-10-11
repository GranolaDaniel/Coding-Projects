from random import randint

def listEnd(myList):
	new_list = []

	new_list.append(myList[0])
	new_list.append(myList[-1])

	print(new_list)
#Function to make a random list of numbers from 0-15 of specified length
def randList():
	num = int(input('Give me the length of this list '))
	ran = []
	
	while len(ran) < num:
		x = randint(0,15)

		ran.append(x)
	return ran

listEnd(randList())
def UserList():
#Make an ordered list of numbers
	user_list = []
	num_list = input("Give me a list of numbers")
	num_list = num_list.split(', ')
	for i in num_list:
		user_list.append(int(i))
	user_list.sort()
	return user_list
def elemSearch(place, search_number):
	for i in place:
		a = False
		if i == search_number:
			print(True)
			a = True
			break
		if i == place[-1] and a != True:
			print(False)
def middleList(aList):
#Returns *element* in middle of list	
	x = len(aList)
	x = floor(x / 2)
	return aList[x]
def binaryElemSearch(place, search_number):
	workingList = []
	while len(place) > 1:	
#Middle element		
		y = middleList(place)
#Middle element index		
		z = place.index(y)
#One spot to the right of the middle number
		cut = (place.index(y) + 1)
#Create binary search loop
		if y == search_number:
			print(True)
			break
		elif y < search_number:
			workingList = place[(z + 1):]
		elif y > search_number:
			workingList = place[:z]

elemSearch(UserList(), 3)

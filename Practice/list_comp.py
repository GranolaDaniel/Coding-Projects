from random import randint

#Create two lists of randm ints (0<=list<=9) to compare
list_a = []
list_b = []

while len(list_a) <= 11:
	list_a.append(randint(0,9))
while len(list_b) <= 13:
	list_b.append(randint(0,9))
#For testing accuracy
#print(list_a, list_b)

#List of common items
common_list = []

#List comparison
for i in list_a:
	if i in list_b:
		common_list.append(i)
#Show items in common
print(common_list)


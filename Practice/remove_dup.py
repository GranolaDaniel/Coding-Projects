from random import randint

#Random set function
def randSet():
	num = int(input('Give me the length of this set '))
	ran = set()
	
	while len(ran) < num:
		x = randint(0,15)

		ran.add(x)
	return ran
def dupeRemove():
	randListA = randSet()
	randListB = randSet()

	remDupes = randListA.intersection(randListB)

	print("Your new set is " + str(remDupes))

dupeRemove()

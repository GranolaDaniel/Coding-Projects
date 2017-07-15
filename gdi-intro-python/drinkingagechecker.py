def isOfDrinkingAge(age):
	if int(age) >= 21:
		print("This person is of drinking age")
	else:
		print("This person is not of drinking age")

isOfDrinkingAge(input('Please type your age '))
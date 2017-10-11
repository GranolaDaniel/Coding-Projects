def revWord():
	x = input("Please give me a string to reverse: ")
	indItems = x.split()
#Reverse list
	x = x[::-1]
#Join the string back in reverse
	revString = " ".join(x)
	print(str(revString))
revWord()
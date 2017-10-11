from random import randint
from random import sample

def passGen():
	passLength = int(input("Please choose a length for your password: "))
	password = []
#Random character generator
#Lists of possible characters
	x = ['0', '1', '3', '4', '5', '6', '7', '8', '9']
	y = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
	z = ['!', '@', '#', '$', '%', '^', '&', '*', '(']
	a = [')', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q']
	b = ['r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	c = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
	d = ['+', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q']
	f = ['R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#Random character from character set	
	while len(password) != passLength:
#Character set and characters 
		charSet = [x, y, z, a, b, c, d, f]
		row = randint(0, 8)
#Randomly choose a character set
		ranCharSet = sample(charSet, 1)
#Randomly choose a character from the random character set
		passChar = ranCharSet[0][row]		
#Add characters to password list		
		password.append(passChar)
	endPass = ''.join(password)
	print(endPass)

passGen()

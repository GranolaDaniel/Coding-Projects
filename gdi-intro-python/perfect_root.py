from math import *

number = int(input('Give me a number '))

if sqrt(number) % 1 != 0:
	print('This number does not have a perfect root')
else:
	print('This number has a perfect root. It is ' + str(sqrt(number)))
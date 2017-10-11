from math import sqrt, ceil

def prime(num):
#Check that num >= 0	
	if num < 0:
		print('You must choose a number that\'s greater than or equal to zero')
		return
	max_root = ceil(sqrt(num))
#Make a list of possible divisors using integers <= num's max root	
	poss_div = []
	n = 3
	while n <= max_root:
		poss_div.append(n)
		n += 1
#Prime check using 2 as divisor (is even)
	if num % 2 == 0:
		print('This number is not prime')
		return
#Prime check using all ints <= max root as divisors	
	else:
		for i in poss_div:
			if num % i == 0:
				print('This number is not prime')
				break
			else:
				print('This number is prime')
				break

get_prime = prime(int(input("Give me a number: ")))
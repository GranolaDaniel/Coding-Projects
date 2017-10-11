from random import randint

ran_num = randint(1000, 9999)
user_guess = 1

while ran_num != user_guess:
#Choose random four digit number for guessing
	user_guess = int(input("Please guess a four-digit number: "))
#Change numbers into strings so they can be iterated
	ran_num_str = str(ran_num)
	user_guess_str = str(user_guess)
#'Cows' and 'bulls' loop
	cows = 0
	bulls = 0
	x = 0
	while x < 4:
		if ran_num_str[x] == user_guess_str[x]:
			cows += 1
		elif ran_num_str[x] == user_guess_str[0] and x != 0:
			bulls += 1
		elif ran_num_str[x] == user_guess_str[1] and x != 1:
			bulls += 1
		elif ran_num_str[x] == user_guess_str[2] and x != 2:
			bulls += 1
		elif ran_num_str[x] == user_guess_str[3] and x != 3:
			bulls += 1
		x += 1
	print(str(cows) + 'cow(s), ' + str(bulls) + 'bull(s)')
	
	if user_guess == ran_num:
		print("You win!")
		break




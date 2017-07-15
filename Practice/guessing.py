from random import randint

rand_num = randint(1,9)

user_guess = ''
num_guess = 0

while user_guess != 'exit' or user_guess != 'Exit':
	user_guess = input('Guess a number between 1 and 9 (type exit to quit): ')
	str_guess = str(user_guess).lower()
#Exit check
	if str_guess == 'exit':
		break
	user_guess = int(user_guess)
#Checking to make sure that user entered a numeral
	if type(user_guess) != int:
		print('That\'s not a valid number. Please type a numeral')
		break
#Comparing user input and random number
	if user_guess == rand_num:
		print('You\'re correct!')
		num_guess += 1
		print('You made ' + str(num_guess) + ' guesses.')
		print('Thanks for playing!')
		break
	elif user_guess < rand_num:
		print('Too low!')
		num_guess += 1
	elif user_guess > rand_num:
		print('Too high!')
		num_guess += 1
#Replay
	replay = input('Would you like to try again? ')
	replay = replay.lower()
	if replay == 'yes':
		continue
	elif replay == 'no':
		print('You made ' + str(num_guess) + ' guesses.')
		print('Thanks for playing!')
		break
	else:
		print('Idk what that means')
		print('You made ' + str(num_guess) + ' guesses.')
		print('Thanks for playing!')
		break
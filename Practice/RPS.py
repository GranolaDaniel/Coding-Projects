#Rock-Paper-Scissors
from random import choice

replay = 'yes'

while replay == 'yes':
	user_choice = input("Choose Rock, Paper, or Scissors ")
	user_choice = user_choice.lower()

	comp_choice = choice(['rock', 'paper', 'scissors'])
#All scenarios
	outcome = ''
#user_choice == 'rock'
	if user_choice == 'rock' and comp_choice == 'rock':
		print('The computer chose ' + comp_choice + '. It\'s a tie!')
		outcome = 'tie'
	elif user_choice == 'rock' and comp_choice == 'paper':
		print('The computer chose ' + comp_choice + '. You lose!')
		outcome = 'lose'
	elif user_choice == 'rock' and comp_choice == 'scissors':
		print('The computer chose ' + comp_choice + '. You win!')
		outcome = 'win'
#user_choice == 'paper'
	elif user_choice == 'paper' and comp_choice == 'rock':
		print('The computer chose ' + comp_choice + '. You win!')
		outcome = 'win'
	elif user_choice == 'paper' and comp_choice == 'paper':
		print('The computer chose ' + comp_choice + '. It\'s a tie!')
		outcome = 'tie'
	elif user_choice == 'paper' and comp_choice == 'scissors':
		print('The computer chose ' + comp_choice + '. You lose!')
		outcome = 'lose'
#user_choice == 'scissors'
	elif user_choice == 'scissors' and comp_choice == 'rock':
		print('The computer chose ' + comp_choice + '. You lose!')
		outcome = 'lose'
	elif user_choice == 'scissors' and comp_choice == 'paper':
		print('The computer chose ' + comp_choice + '. You win!')
		outcome = 'win'
	elif user_choice == 'scissors' and comp_choice == 'scissors':
		print('The computer chose ' + comp_choice + '. It\'s a tie!')
		outcome = 'tie'
#user_choice != any options
	else:
		print(user_choice + ' is not a valid option. Please select again.')
#Checking if the user wants to play again	
	replay = str(input('Would you like to play again? Type yes or no: '))
	replay = replay.lower()

	if replay == 'yes':
		continue 
	elif replay == 'no':
		break
	else:
		print('Idk what that means!')
		break
print('Thanks for playing!')
from random import choice

def hangmanGame():
	with open('sowpods.txt', 'r') as f:
		line = f.readlines()
		selected_word = choice(line)
		selected_word = selected_word.strip()
#Word is a complete list of characters from the word to be guessed
#working_list is an empty list that will be updated after a correct guess
	word = list(selected_word)
	unders = ['_' for x in word]
	working_list = unders
	s = ' '
	unders_show = s.join(unders)

	print('Welcome to Hangman!')
	print(unders_show)

	num_inc_guesses = 0
	guessed_letters = []

	while working_list != word and num_inc_guesses != 6:
		guess = input('Guess a letter: ')
		guess = guess.upper()

		if guess in guessed_letters:
			print('You\'ve already guessed that letter. Try again!')
			continue
		for i, char in enumerate(word):
			if char == guess:
				working_list[i] = char
			elif guess not in word:
				num_inc_guesses += 1
				print('Incorrect. You have ' + str(6 - num_inc_guesses) + ' remaining.')
				break
		guessed_letters.append(guess)
		print(s.join(working_list))		
	if num_inc_guesses == 6:
		print('You\' re out of guesses! The word is: ' + selected_word)
	else:
		print('You win! Thanks for playing!')
	
	again = input('Type y if you would like to play again: ')
	if again == 'y' or again == 'Y':
		hangmanGame()
	else:
		print('Thanks for playing!')

hangmanGame()
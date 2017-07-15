from random import randint

computer_number = randint(0,10)

input("Guess the number!")

if (input == computer_number) : print("You\'re right!")
else: print("Nope! It was " + str(computer_number))
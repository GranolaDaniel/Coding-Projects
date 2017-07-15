def birthdayDict():

	birth_dict = {
		"Brian": '11/19/1992',
		"Lady": '3/28/1960',
		"Guy": '6/14/1996'
	}

	print('Welcome to the birthday dictionary program. I know the birthdays of: ' + str(birth_dict.keys()))

	usr_inp = input('Who\'s birthday do you want to look up? ')
	
	b = birth_dict[usr_inp]

	print('{}\'s birthday is {}.'.format(usr_inp, b))

birthdayDict()

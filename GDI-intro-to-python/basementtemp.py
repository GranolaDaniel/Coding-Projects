def basementIsOk(temperature, humidity):
	if int(temperature) < 50 or int(humidity) > 70:
		print('The basement is not okay!')
	else:
		print('The basement is fine, you spazz')

basementIsOk(input('What\'s the temperature? '), input('What\'s the humidity? '))
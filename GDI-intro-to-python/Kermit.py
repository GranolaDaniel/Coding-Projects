def willKermitPlantFlowers(dayOfWeek, season, currentTemperature):
	if dayOfWeek != 'Saturday':
		print('Kermit will nto be planting flowers today')
	elif season != 'Spring':
		print('Kermit will not be planting flowers today')
	else:
		print('Kermit will be planting flowers today')

willKermitPlantFlowers(input('What is today? '), input('What season is it? '), input('What\'s the temperature? '))
def maxThree(num1, num2, num3):
	num1 = int(num1)
	num2 = int(num2)
	num3 = int(num3)
	
	if num1 > num2 and num3:
		return num1
	elif num2 > num1 and num3:
		return num2
	elif num3 > num1 and num2:
		return num3

x = maxThree(2, 6, 5)
print(x)
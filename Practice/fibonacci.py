def fibonacci():
	num = int(input('Give me the length of the Fibonacci sequence: '))
	fib = [1, 1]
	n = len(fib)
	
	while n != num:
		a = fib[-1] + fib[-2]
		fib.append(a)
		n += 1
	print(fib)

if __name__ == "__main__":
	fibonacci()
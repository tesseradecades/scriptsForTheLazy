def fibonacci(n=0):
	if(n == 0 or n == 1):
		return n
	else:
		return fibonacci(n-1) + fibonacci(n-2)

def main():
	for x in range(0,13):
		print(fibonacci(x))

if __name__ == "__main__":
	main()
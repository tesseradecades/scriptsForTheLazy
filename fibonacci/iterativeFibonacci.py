def fibonacci(n=0):
	a, b = 0, 1
	for i in range(0, n):
		a, b = b, a + b
	return a

def main():
	for x in range(0,13):
		print(fibonacci(x))

if __name__ == "__main__":
	main()
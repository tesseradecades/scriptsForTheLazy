import iterativeFibonacci,math,recursiveFibonacci, time
import matplotlib.pyplot as plt
from memory_profiler import memory_usage

def plotRuns(xVals, yVals):
	plt.plot(xVals, yVals, 'ro')
	plt.axis([0, len(xVals)-1, 0, math.ceil(max(yVals))])
	plt.show()

def main():
	maxFib = 40
	fibNums = range(0,maxFib+1)
	runs = 10
	itTimes = [0]*(maxFib+1)
	itMems = [0]*(maxFib+1)
	reTimes = [0]*(maxFib+1)
	reMems = [0]*(maxFib+1)
	for i in range(1,runs+1):
		print("Run#"+str(i))
		for x in fibNums:
			start = time.time()
			iterativeFibonacci.fibonacci(x)
			end = time.time()
			elapsed = end - start
			printString = str(x)+":\tIterative:\tTime:\t"+str(elapsed)
			itTimes[x]+=elapsed
			itMems[x]+= max( memory_usage( ( iterativeFibonacci.fibonacci, (x,) ) ) )
			print(printString)

		for x in fibNums:
			start = time.time()
			recursiveFibonacci.fibonacci(x)
			end = time.time()
			elapsed = end - start
			printString = str(x)+":\tRecursive:\tTime:\t"+str(elapsed)
			reTimes[x]+=elapsed
			reMems[x]+= max(memory_usage((recursiveFibonacci.fibonacci, (x,))))
			print(printString)
	for x in itTimes:
		x = x/runs
	for x in itMems:
		x = x/runs
	for x in reTimes:
		x = x/runs
	for x in reMems:
		x = x/runs

	plotRuns(fibNums,itTimes)
	plotRuns(fibNums,itMems)
	plotRuns(fibNums,reTimes)
	plotRuns(fibNums,reMems)
	
if __name__ == "__main__":
	main()
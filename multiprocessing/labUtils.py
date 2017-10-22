import timeit, functools
import matplotlib.pyplot as plt
from memory_profiler import memory_usage,profile

def plotRuns(xVals, yVals):
	plt.plot(xVals, yVals, 'ro')
	plt.axis([0, len(xVals)-1, 0, math.ceil(max(yVals))])
	plt.show()

def writeOutputFile(vals, fileName, arg="a+"):
	f = open(fileName, arg)
	f.write(str(vals))
	f.close()

def getAvgMemory(method, arg, iterations):
	mems = []
	for x in range(0,iterations):
		mems+=memory_usage((method, (arg,)))
	return sum(mems)/len(mems)

def memoizeMethod(method, arg, iterations):
	command = str(method)
	avgMem = getAvgMemory(method, arg, iterations)
	memOutString = "Average "+command+" memory:\t"+str(avgMem)+"KB\tOver "+str(iterations)+" iterations.\n"
	print(memOutString)
	writeOutputFile(memOutString,"output/memory.txt")
	
def timeMethod(method, arg, iterations):
	command=str(method)
	t = timeit.Timer(functools.partial(method, arg))
	avgTime = t.timeit(iterations)/iterations
	timeOutString = "Average "+command+" time:\t"+str(avgTime)+"seconds\tOver "+str(iterations)+" iterations.\n"
	print(timeOutString)
	writeOutputFile(timeOutString,"output/time.txt")
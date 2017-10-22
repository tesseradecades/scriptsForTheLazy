import labUtils, quickSort, primes



def testQuickSortJobs(jobs, input):
	labUtils.timeMethod(quickSort.quickSort, input, jobs)
	labUtils.memoizeMethod(quickSort.quickSort, input, jobs)

def testMQuickSortJobs(jobs, input):
	labUtils.timeMethod(quickSort.mQuickSort, input, jobs)
	labUtils.memoizeMethod(quickSort.mQuickSort, input, jobs)

def testIsPrime(jobs, input):
	labUtils.timeMethod(primes.is_primeHelp, input, jobs)
	labUtils.memoizeMethod(primes.is_primeHelp, input, jobs)

def testMIsPrime(jobs, input):
	labUtils.timeMethod(primes.m_is_primeHelp, input, jobs)
	labUtils.memoizeMethod(primes.m_is_primeHelp, input, jobs)

def main():
	j = 10
	test = [1,7,5,8,2,4,9,3,6,0]
	primeTests=[7,97,997,9973]
	#print(test)
	#print(10**2)
	#testQuickSortJobs(j,test)
	
	for x in range(0,4):
		pTest = test * (10**x)
		testQuickSortJobs(j,pTest)
		testMQuickSortJobs(j,pTest)
		testIsPrime(j, primeTests[x])
		testMIsPrime(j,primeTests[x])
	
if __name__=="__main__":
	main()
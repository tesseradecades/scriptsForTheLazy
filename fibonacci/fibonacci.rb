require 'memory_profiler'
require 'squid'

def iterativeFibonacci(n)
	a, b = 0, 1
	for i in (0..n-1) do
		a, b = b, a+b
	end
	return a
end

def plotRuns(xVals, yVals, pdfName)
	Prawn::Document.generate pdfName do
		data = {'Times' => xVals.zip(yVals).to_h}
		chart data, type: :point, steps: yVals.max.ceil+1
	end
end

def recursiveFibonacci(n)
	if n == 0 or n == 1
		return n
	else
		return recursiveFibonacci(n-1)+recursiveFibonacci(n-2)
	end
end

def main()
	maxFib=40
	fibNums= Array(0..maxFib)
	runs=10
	itTimes = Array.new(maxFib, 0)
	itRetMems = Array.new(maxFib, 0)
	itMems = Array.new(maxFib, 0)
	reTimes = Array.new(maxFib, 0)
	reRetMems = Array.new(maxFib, 0)
	reMems = Array.new(maxFib, 0)
	for i in (1..runs) do
		puts("Run#"+i.to_s)
		for x in fibNums do
			start = Time.now
			iterativeFibonacci(x)
			endTime = Time.now
			elapsed = endTime - start
			itTimes[x] = itTimes[x].to_i+elapsed
			report = MemoryProfiler.report do
				iterativeFibonacci(x)
			end
			totMem = report.total_allocated_memsize
			retMem = report.total_retained_memsize
			itMems[x] = itMems[x].to_i+totMem
			itRetMems[x] = itRetMems[x].to_i+retMem
			printString = x.to_s+":\tIterative:\tTime:\t"+elapsed.to_s+"\tTotal Allocated Memory:\t"+totMem.to_s+"\tTotal Retained Memory:\t"+retMem.to_s
			puts(printString)
		end
		for x in fibNums do
			start = Time.now
			recursiveFibonacci(x)
			endTime = Time.now
			elapsed = endTime - start
			reTimes[x] = reTimes[x].to_i+elapsed
			report = MemoryProfiler.report do
				recursiveFibonacci(x)
			end
			totMem = report.total_allocated_memsize
			retMem = report.total_retained_memsize
			reMems[x] = reMems[x].to_i+totMem
			reRetMems[x] = reRetMems[x].to_i+retMem
			printString = x.to_s+":\tRecursive:\tTime:\t"+elapsed.to_s+"\tTotal Allocated Memory:\t"+totMem.to_s+"\tTotal Retained Memory:\t"+retMem.to_s
			puts(printString)
		end
	end
	for x in itTimes do
		x = x/runs
	end
	for x in itMems do
		x = x/runs
	end
	for x in itRetMems do
		x = x/runs
	end
	for x in reTimes do
		x = x/runs
	end
	for x in reRetMems do
		x = x/runs
	end
	for x in reMems do
		x = x/runs
	end
	plotRuns(fibNums, itTimes, 'itTimes.pdf')
	plotRuns(fibNums, itRetMems, 'itRetMems.pdf')
	plotRuns(fibNums, itMems, 'itMems.pdf')
	plotRuns(fibNums, reTimes, 'reTimes.pdf')
	plotRuns(fibNums, reRetMems, 'reRetMems.pdf')
	plotRuns(fibNums, reMems, 'reMems.pdf')
end

main()
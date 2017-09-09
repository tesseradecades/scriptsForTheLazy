from copy import deepcopy
import random, string, time


outputTimeFileName = "times.txt"

"""
Sorting algorithms courtesy of geeksforgeeks.org
"""
def bubbleSort(arr=[]):
	n = len(arr)
	for i in range(n):
		for j in range(0, n-i-1):
			if(arr[j] > arr[j+1]):
				arr[j], arr[j+1] = arr[j+1], arr[j]

# A function to do counting sort of arr[] according to
# the digit represented by exp.
def countingSort(arr, exp1):
 
    n = len(arr)
 
    # The output array elements that will have sorted arr
    output = [0] * (n)
 
    # initialize count array as 0
    count = [0] * (10)
 
    # Store count of occurrences in count[]
    for i in range(0, n):
        index = int((arr[i]/exp1))
        count[ (index)%10 ] += 1
 
    # Change count[i] so that count[i] now contains actual
    #  position of this digit in output array
    for i in range(1,10):
        count[i] += count[i-1]
 
    # Build the output array
    i = n-1
    while i>=0:
        index = (arr[i]/exp1)
        output[ int(count[ int((index)%10) ] - 1)] = arr[i]
        count[ int((index)%10) ] -= 1
        i -= 1
 
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0,len(arr)):
        arr[i] = output[i]
				
def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
def merge(arr, l, m, r):
    n1 = int(m - l + 1)
    n2 = int(r- m)
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0 , n1):
        L[i] = arr[int(l + i)]
 
    for j in range(0 , n2):
        R[j] = arr[int(m + 1 + j)]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = int(l)     # Initial index of merged subarray
 
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort(arr,l,r):
    if l < r:
 
        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = (l+(r-1))/2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

def partition(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low , high):
 
        # If current element is smaller than or
        # equal to pivot
        if   arr[j] <= pivot:
         
            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )
 
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
def quickSort(arr,low,high):
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

# Method to do Radix Sort(doesn't work for strings)
def radixSort(arr):
	# Find the maximum number to know number of digits
	max1 = max(arr)
	# Do counting sort for every digit. Note that instead
	# of passing digit number, exp is passed. exp is 10^i
	# where i is current digit number
	exp = 1
	while max1/exp > 0:
		countingSort(arr,exp)
		exp *= 10

def swap(x,y):
	z = x
	x = y
	y = z

"""END OF SORTING ALGORITHMS"""
def driver(maxMag=0, type="i"):
	for x in range(0, maxMag+1):
		randData = generateData(x, type)
		maxVal = [max(randData)]
		minVal = [min(randData)]
		maxFirst = maxVal+deepcopy(randData)
		maxLast = deepcopy(randData)+maxVal
		minFirst = minVal+deepcopy(randData)
		minLast = deepcopy(randData)+minVal
		
		f = open(outputTimeFileName, "a+")
		writeString = "\n10^"+str(x)+" data\n"
		writeString+="Random\n"+generateWriteString(randData,x)
		writeString+="Max First\n"+generateWriteString(maxFirst,x)+"\n"
		writeString+="Max Last\n"+generateWriteString(maxLast,x)+"\n"
		writeString+="Min First\n"+generateWriteString(minFirst,x)+"\n"
		writeString+="Min Last\n"+generateWriteString(minLast,x)+"\n"
		f.write(writeString)
		print(writeString)
		f.close()

def generateData(m, t):
	print("Generating data for a magnitude of ", m)
	l = []
	mag = 10**m
	if( t == "i"):
		for x in range(0,mag):
			l.append(random.randrange(mag))
	elif( t == "s"):
		l.append(randString(random.randrange(10)))
	f = open("generatedData.txt", "a+")
	writeString = "Magnitude: "+str(m)+" \nRandomData\nData: "+str(l)+"\n"
	f.write(writeString)
	#print(writeString)
	f.close()
	print("Finished generating data for a magnitude of ", m)
	return l

def generateWriteString(data, mag):
	writeString=""
	if(mag < 6):
		writeString+=testSorts(deepcopy(data), "Bubble")
		writeString+=testSorts(deepcopy(data), "Insertion")
	writeString+=testSorts(deepcopy(data), "Merge")
	writeString+=testSorts(deepcopy(data), "Quick")
	if(mag < 7):
		writeString+=testSorts(deepcopy(data), "Radix")
	return writeString

def randString(size=10, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for x in range(size))

def testSorts(arr, type):
	print("Running "+type+" Sort")
	start = time.time()
	if(type == "Bubble"):
		start = time.time()
		bubbleSort(arr)
	elif(type == "Insertion"):
		insertionSort(arr)
	elif(type == "Merge"):
		mergeSort(arr, 0, len(arr)-1)
	elif( type == "Quick"):
		quickSort(arr, 0, len(arr)-1)
	elif(type=="Radix"):
		radixSort(arr)
	end = time.time()
	print(type+" Sort finished")
	elapsed = (end - start)
	retString = type+" Sort time "+str(elapsed)+"\n"
	return retString

"""
First argument for maximum order of magnitude you want to test, second for the 
kind of data (i or s)
"""
driver(10, "i")

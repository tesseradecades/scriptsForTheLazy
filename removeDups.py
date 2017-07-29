import random

"""
method to remove duplicate entries from a list. based on the quicksort algorithm
the first occurrence of a random entry in the list is chosen, then every entry
prior to the chosen entry is put in a left list to be deduped, and every entry to
the right, not including entries identical to the pivot is put in a right list
to be deduped. The returned list is a concatenation of the left list, a list
containing only the pivot, and the right list. It has similar downsides to the
quicksort algorithm.

If the pivot index is 0:
	The right list will have a size of N-1 and that level of recursion will
	require O(N) time to complete
"""
def removeDups(dupList=[]):
	if(len(dupList)==0):
		return dupList
	
	pivot = dupList[random.randint(0,len(dupList)-1)]
	pivotIndex = dupList.index(pivot)
	
	"""
	Since the pivot is the leftmost occurrence of a random entry, there are no
	duplicates of the pivot to the left of it
	"""
	left=dupList[:pivotIndex]
	right=[]
	
	for d in dupList[pivotIndex:]:
		if pivot != d and dupList.index(d) > pivotIndex:
			right.append(d)
	
	return (removeDups(left) + [pivot] + removeDups(right))
	
def main():
	dL = [5,8,2,4,1,7,4,3,2,1,9,8,7,6,5]
	dL += dL*random.randint(1,11)
	random.shuffle(dL)
	print(dL)
	print(removeDups(dL))

if __name__=="__main__":
	main()
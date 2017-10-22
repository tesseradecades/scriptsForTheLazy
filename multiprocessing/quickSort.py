__author__="Nathan Evans"
from multiprocessing import Process

def chooseMiddle(f,m,l):
	#if m is the middle
	if( (f <= m and m <=l) or (f >= m and m >=l) ):
		return m
	#if f is the middle
	elif( (m <= f and f <=l) or (m >= f and f >=l) ):
		return f
	#otherwise, l is the middle
	else:
		return l
	

def mQuickSort(l):
	if(len(l) < 2):
		return l
	else:
		lLength = len(l)
		len2 = lLength//2
		pivot = chooseMiddle(l[0],l[len2],l[lLength-1])
		
		less = []
		eq = []
		more = []
		for x in l:
			if(x < pivot):
				less.append(x)
			elif(x==pivot):
				eq.append(x)
			else:
				more.append(x)
		pL = Process(target=mQuickSort, args=(less,))
		pM = Process(target=mQuickSort, args=(more,))
		
		#return mQuickSort(less)+eq+mQuickSort(more)
		pL.start()
		pM.start()
		pL.join()
		pM.join()
	
def quickSort(l):
	if(len(l) < 2):
		return l
	else:
		lLength = len(l)
		len2 = lLength//2
		pivot = chooseMiddle(l[0],l[len2],l[lLength-1])
		
		less = []
		eq = []
		more = []
		for x in l:
			if(x < pivot):
				less.append(x)
			elif(x==pivot):
				eq.append(x)
			else:
				more.append(x)
		return quickSort(less)+eq+quickSort(more)

def main():
	enneaList =[1,7,5,8,2,4,9,3,6,0]
	print(quickSort(enneaList))
	mQuickSort(enneaList)
	
if __name__ =="__main__":
	main()
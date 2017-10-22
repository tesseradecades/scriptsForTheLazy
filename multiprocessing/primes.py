__author__="Nathan Evans"
import math
from multiprocessing import Process

def isPrime(n, p):
	for x in p:
		if(n % x == 0):
			return False
	return True

def is_primeHelp(n):
	return is_prime(2,n)
	
def is_prime(a,N):
    #print(a, N)
    if N <= 1:
        return True
    else:
        if a >= N:
            return True#print(N)
        else:
            if N == 2: 
                return True#print(N)
            elif (N % a) == 0:
                return False
            else:
                return is_prime(a+1,N)

    return False

def m_is_primeHelp(n):
	return m_is_prime(2,n)
	
def m_is_prime(a,N):
	if N <= 1:
		return True
	else:
		if a >= N:
			return True#print(N)
		else:
			if N == 2: 
				return True#print(N)
			elif (N % a) == 0:
				return False
			else:
				p = Process(target=is_prime, args=(a+1,N,))
				p.start()
				p.join()
	return False

def primes(n):
	p = []
	if(n <= 2):
		return p
	else:
		for x in range(2,n):
			if(isPrime(x,p)):
				p.append(x)
	return [1]+p



def main():
	print(primes(10))
	"""print(is_prime(2, 7))#  => True
	print(is_prime(2, 4))#  => False
	print(is_prime(2, 37))
	m_is_prime(2,97)"""

if __name__=="__main__":
	main()
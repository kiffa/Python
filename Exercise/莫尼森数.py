import time
import math
 
def prime(num):
	l1 = [2]
	for i in range(3, int(math.sqrt(num)+1), 2):
		if num % i ==0:
			return False
	return num
 
def monisen(no):
	l2 = [2]
	a = 3
	while 1 :
		P = prime(a)
		if P == False:
			a = a+2
			continue
		M = 2**P-1
		if prime(M) == False:
			a = a+2
		else:
			l2.append(M)
			a+=2
		if len(l2) == no:
			break
	return l2[-1]
 
start = time.clock()
 
print(monisen(6), end="  ")
 
end = time.clock()
print("Time = %f s" % (end - start))

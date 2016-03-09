import random
def Divisors(n):
	divisors = []
	for i in range(1,((n/2)+1)):
		if (n % i == 0):
			divisors.append(i) 
	return divisors
a = random.choice(Divisors(10));
print a



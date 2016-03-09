import random

case = []
# FUNCTION TO FIND DIVISORS
def Divisors(n):
	divisors = []
	for i in range(1,((n/2)+1)):
		if (n % i == 0):
			divisors.append(i) 
	return divisors

# TAKE NO OF TEST CASES
T = input()

# TAKE USER INPUTS
for i in range (0,T):
	case.append(input())

# OUTPUT SOLUTION

for N in case:
	while(N > 0):
		if N == 1:
			print "BOB"
			break;
		else:
			N = N - random.choice(Divisors(N))
			#print N


		if N == 1:
			print "ALICE"
			break;
		else: 
			N = N - random.choice(Divisors(N))
			#print N
 

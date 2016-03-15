


def get_sum(a,b):
	sum = 0
	if a!=b:
		for i in xrange(min(a,b),max(a,b)+1):
			print i
			sum = sum+i
		return sum
	else:
		return a
p=get_sum(1,0)
print p
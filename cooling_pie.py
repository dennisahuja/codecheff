def no_of_pies(N,pie_weight,total_pie,rack_cap,total_rack):
	count = N
	if rack_cap >= pie_weight:
		print N
		return(N)
	else:
		total_pie = total_pie - max(pie_weight)
		pie_weight.remove(max(pie_weight))
		N = N-1
		no_of_pies(N,pie_weight,total_pie,rack_cap,total_pie)







T = input()
for t in xrange(T):
	N = input()
	pie_weight = []
	rack_cap = []
	total_pie,total_rack = 0,0
	for n in xrange(N):
		pie = input()
		pie_weight.append(pie)
		total_pie = total_pie + pie

	for n in xrange(N):
		rack = input()
		rack_cap.append(rack)
		total_rack = total_rack + rack
	no_of_pies(N,pie_weight,total_pie,rack_cap,total_rack)


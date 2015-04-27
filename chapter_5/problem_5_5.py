def bit_diff(a,b):
	a = str(bin(a))[2:]
	b = str(bin(b))[2:]
	a_sum = 0
	b_sum = 0
	for i in a:
		if i == '1':	
			a_sum += 1
	for i in b:
		if i == '1':
			b_sum += 1
	return abs(a_sum-b_sum)
	
print bit_diff(31,14) 

def cmbn(n,m,i,j):
	n = str(n)[::-1]
	m = str(m)[::-1]
	s = n[:i] + m + n[j + 1:]
	return int(s[::-1])

print cmbn(10000000000,10011,2,6)



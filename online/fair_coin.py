"""
You toss a fair coin 400 times. What is the probability that you get at least 220 heads? Round to the nearest percent.
"""

def ch(n,r):
	if r == 0:
		return 1
	mx = max(r,n-r)
	mn = min(r,n-r)
	i = 0
	nm = 1
	while i < mn:
		nm = (n - i) * nm
		i += 1
	i = 1
	dm = 1
	while i <= mn:
		dm = i * dm
		i += 1
	return nm/dm

def bin_dist(n,k,p):
	return ch(n,k) * p**k * (1-p)**(n-k)

print bin_dist(4,2,.5) 

def add_prb(t,s,p):
	total = 0
	while s <= t:
		total = total + bin_dist(t,s,p)
		s += 1
	return total

print add_prb(11,6,.5) 


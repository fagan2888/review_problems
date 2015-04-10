def make_d(s):
	d = {}
	for e in s:
		if e in d.keys():
			d[e] = d[e] + 1
		else:
			d[e] = 1
	return d

def p(s1,s2):
	if len(s1) != len(s2):
		return False
	d1 = make_d(s1)
	d2 = make_d(s2)
	if d1 == d2:
		return True
	return False

s1 = '1234'
s2 = '4221'

print p(s1,s2)


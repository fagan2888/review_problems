#

def init_a(l):
	a = []
	for i in range(l):
		a.append(i)
	return a

def union(a,x,y):
	x = a[x]
	for i in range(len(a)):
		if a[i] == x:
			a[i] = a[y]
	return a

def connected(a,x,y):
	if a[x] == a[y]:
		return True
	else:
		return False

a = init_a(10)
a = union(a,4,3)
print a
a = union(a,3,8)
print a
a = union(a,6,5)
print a
a = union(a,9,4)
print a
a = union(a,2,1)
print a
print connected(a,8,9)
print connected(a,5,0)
a = union(a,5,0)
print a
a = union(a,7,2)
print a
a = union(a,6,1)
print a

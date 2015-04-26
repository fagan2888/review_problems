def z(x):
	z_rows = set()
	z_cols = set()
	m = len(x)
	n = len(x[0])
	for r in range(m):
		for c in range(n):
			if x[r][c] == 0:
				z_rows.add(r)
				z_cols.add(c)
	for e in z_rows:
		x[e] = [0] * n
	for e in z_cols:
		for i in range(m):
			x[i][e] = 0
	return x

x = [[1,1,1],[1,0,1]]

print z(x)

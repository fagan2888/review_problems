def rot_x(x):
	n = len(x)
	for l in range(n/2):
		fst = l
		lst = n - l - 1
		for i in range(fst,lst):
			j = i - fst
			print i,j
			#save top
			tmp = x[fst][i]
			#top << left
			x[fst][i] = x[lst - j][fst]
			#left << bottom
			x[lst - j][fst] = x[lst][lst - j]
			#bottom << right
			x[lst][lst - j] = x[i][lst]
			#replace right
			x[i][lst] = tmp

x = [['00','01','02','03'],['10','11','12','13'],['20','21','22','23'],['30','31','32','33']]

rot_x(x)

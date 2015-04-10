def rotate_grid(N):
	n = len(N)
	s = n - 1
	new_grid = []
	for i in range(n):
		new_grid.append([])
		for j in range(n):
			new_grid[i].append(N[s-j][i])
	return new_grid

def rotate_in_place(N):
	pass


N = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

print rotate_grid(N)

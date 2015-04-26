class Towers_of_Hanoi(object):
	def __init__(self,size):
		self.towers = [[],[],[]]
		self.towers[0] = [x + 1 for x in range(size)[::-1]]
		print self

	def __str__(self):
		return str(self.towers)

	def move_tower(self,size=None,f=0,h=1,t=2):
		if size is None:
			size = len(self.towers[0])
		if size == 1:
			self.towers[t].append(self.towers[f].pop())
			print self
		else:
			self.move_tower(size - 1,f,t,h)
			self.move_tower(1,f,h,t)
			self.move_tower(size - 1,h,f,t)	

t = Towers_of_Hanoi(3)
t.move_tower()

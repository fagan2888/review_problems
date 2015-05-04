"""best estimated path cost first (A*)"""

class Graph(object):
	def __init__(self,h,a):
		self.h = h
		self.a = a
		self.p = []
		self.v = set() 
		self.f = {} #item:path,cost
	def __str__(self):
		return ' -> '.join(self.p)
	def get_path(self,orig,dest):
		self.p = self.travel(orig,dest)
		return self
	def get_frontier(self,orig):
		path = self.f[orig]['path']
		cost = self.f[orig]['cost']
		for dest in self.a[orig]:
			if dest not in self.v:
				dist = self.a[orig][dest]
				self.f[dest] = {'path':path + [dest],'cost': cost + dist,'heur':cost + dist + self.h[dest]}
				print dest, self.f[dest]
	def travel(self,orig,dest):
		if orig == dest: return self.f[orig]['path']
		if not self.f and not self.v:
			self.f[orig] = {'path':[orig],'cost':0}
		self.get_frontier(orig)
		self.v.add(orig)
		del self.f[orig]
		min_heur = None 
		for item in self.f:
			if min_heur is None:
				min_heur = self.f[item]['heur']
				next_dest = item
			else:
				if self.f[item]['heur'] < min_heur: 
					min_heur = self.f[item]['heur']
					next_dest = item
		print 'frontier', self.f.keys()
		return self.travel(next_dest,dest)
		
#Example
h = {'Arad':366,'Timisoara':329,'Zerind':374,'Oradea':380,'Sibiu':253,'Fagaras':176,'Rimnicu':193,'Pitesti':100,'Craiova':160,'Bucharest':0,'Nowhere':266}
a = {'Arad' : {'Nowhere':100,'Timisoara':118,'Zerind':75,'Sibiu':140},'Timisoara':{'Arad':118,'Craiova':376},'Craiova':{'Rimnicu':146,'Timisoara':376,'Pitesti':138},'Zerind':{'Arad':75,'Oradea':71},'Oradea':{'Sibiu':151,'Zerind':71},'Sibiu':{'Arad': 140,'Oradea':151,'Fagaras':99,'Rimnicu':80},'Fagaras':{'Sibiu':99,'Bucharest':211},'Rimnicu':{'Sibiu':80,'Craiova':146,'Pitesti':97},'Pitesti':{'Rimnicu':97,'Craiova':138,'Bucharest':101},'Bucharest':{'Fagaras':211,'Pitesti':101},'Nowhere':{'Arad':100}}

Hungary = Graph(h,a)
print Hungary.get_path('Craiova','Bucharest')



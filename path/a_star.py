"""best estimated path cost first (A*)"""

class Graph(object):
	def __init__(self,h,a):
		self.h = h
		self.a = a
		self.p = []
		self.visited = set() 
		self.frontier = {}
	def __str__(self):
		return ' -> '.join(self.p)
	def get_cost(self,orig,dest):
		print 'cost from ',orig,' to ',dest,self.h[dest] + self.a[orig][dest]
		return self.h[dest] + self.a[orig][dest]
	def find_path(self,orig):
		min_path = None
		path = ''
		for dest in self.a[orig]:
			if min_path is None:
				min_path = self.get_cost(orig,dest) 
				path = dest
			else:
				curr_path = self.get_cost(orig,dest) 
				if curr_path < min_path:
					min_path = curr_path 
					path = dest 
		return path
	def travel(self,orig,dest):
		self.p.append(orig)
		city = ''
		i = 0
		while city != dest and i < 10:
			print orig
			path = self.find_path(orig)
			self.p.append(path)
			city = path
			orig = path
			i += 1
		return self

h = {'Arad':366,'Timisoara':329,'Zerind':374,'Oradea':380,'Sibiu':253,'Fagaras':176,'Rimnicu':193,'Pitesti':100,'Craiova':160,'Bucharest':0,'Nowhere':266}
a = {'Arad' : {'Nowhere':100,'Timisoara':118,'Zerind':75,'Sibiu':140},'Timisoara':{'Arad':118,'Craiova':376},'Craiova':{'Rimnicu':146,'Timisoara':376,'Pitesti':138},'Zerind':{'Arad':75,'Oradea':71},'Oradea':{'Sibiu':151,'Zerind':71},'Sibiu':{'Arad': 140,'Oradea':151,'Fagaras':99,'Rimnicu':80},'Fagaras':{'Sibiu':99,'Bucharest':211},'Rimnicu':{'Sibiu':80,'Craiova':146,'Pitesti':97},'Pitesti':{'Rimnicu':97,'Craiova':138,'Bucharest':101},'Bucharest':{'Fagaras':211,'Pitesti':101},'Nowhere':{'Arad':100}}

Hungary = Graph(h,a)
#grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#print Hungary.get_cost('Arad','Zerind')
#print  Hungary.get_cost('Sibiu','Rimnicu')

print Hungary.travel('Arad','Bucharest')



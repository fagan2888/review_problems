class Node(object):
	def __init__(self,array,index):
		#array.append(value)
		self.value = array[index]
		self.left = array[2 * index + 1]
		self.right = array[2 * index + 2]

class Heap(object):
	def __init__(self):
		self.values = []
		self.root = None
	def push(self,value):
		l = len(self.values)
		self.values.append(value)
		if self.root is None:
			#self.root = self.values[0]
			self.root = Node(self.values,l)
	def __str__(self):
		return str(self.values)

h = Heap()
print h
h.push(1)
h.push(2)
h.push(3)
print h.root
print h.root.right

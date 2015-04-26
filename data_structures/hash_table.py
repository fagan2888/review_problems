class HashTable(object):
	def __init__(self,size=8):
		self.size = size
		self.keys = [None] * self.size
		self.values = [None] * self.size
		self.u = 0 #table utilization
	def __str__(self):
		ht = []
		for i in range(self.size):
			if self.keys[i] is not None:
				ht.append("' : '".join([self.keys[i],self.values[i]]))
		return "{'" + "','".join(ht) + "'}"
	def add(self,key,value):
		if (self.u * 100)/(self.size) > 60:
			print 'time to resize'
			self.resize_table()
		h = self.hash_key(key)
		for i in range(self.size):
			n =(h + i) % self.size 
			if self.keys[n] is None:
				self.keys[n] = key
				self.values[n] = value
				self.u += 1
				return True
			if self.keys[n] == key:
				print 'already in table'
				return False
	def get(self,key):
		h = self.hash_key(key)
		for i in range(self.size):
			n = (h + i) % self.size
			if self.keys[n] == key:
				return self.values[n]
	def hash_key(self,key):
		s = 0
		for e in key:
			s = s + ord(e)
		return s % self.size
	def resize_table(self):
		n_ht = HashTable(self.size * 4)
		for key in self.keys:
			if key is not None:
				n_ht.add(key,self.get(key))
		self.size = n_ht.size
		self.keys = n_ht.keys
		self.values = n_ht.values
		self.u = n_ht.u
			
ht = HashTable()
ht.add('duck','a')
ht.add('duck','b')
ht.add('goose','c')
ht.add('google','d')
ht.add('stables','e')
ht.add('google','f')
ht.add('mouse','g')
ht.add('sloth','h')
ht.add('eagle','i')
ht.add('hawk','j')
ht.add('john','snow')
ht.add('ned','stark')
print ht
print ht.get('john')


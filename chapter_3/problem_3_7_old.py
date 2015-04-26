class AnimalQueue(object):
	
	def __init__(self):
		from collections import deque
		self.q = deque()
		self.time_stamp = 0
	def __str__(self):
		return str(self.q)
	def en_q(self,animal):
		if animal == "dog" or animal == "cat":
			self.q.append(animal)
			self.time_stamp += 1
		else:
			print "error : invalid animal"

	def de_q(self,animal=None):
		if animal is None:
			return animal.popleft()
		return self.get_animal(animal)

	def get_animal(self, a):
		if a != "dog" and a != "cat":
			return "invalid animal"
		if self.q[0] == a:
			return self.q.popleft()

		v = "animal not in queue"
		c = []
		for e in self.q:
			if e == a:
				v = self.q.popleft()
				break
			else:
				c = self.q.popleft()
		for e in c:
			self.q.appendleft(e)
		return v

		"""
		r = range(len(self.q))
		for i in r:
			if self.q[i] == a:
				return self.q.pop(i)
		return a + " not in queue"
		"""
a = AnimalQueue()
a.en_q("cat")
a.en_q("dog")
a.en_q("dog")
a.en_q("cat")
a.en_q("dog")
a.de_q("cat")
print a
a.de_q("cat")
print a

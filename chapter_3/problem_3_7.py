class AnimalQueue(object):
	
	def __init__(self):
		from collections import deque
		self.dog_q = deque()
		self.cat_q = deque()
		self.time_stamp = 0

	def __str__(self):
		return "dog_q : " + str(self.dog_q) + ", cat_q : " + str(self.cat_q)

	def en_q(self,animal):
		self.time_stamp += 1
		if animal == "dog":
			self.dog_q.append([animal,self.time_stamp])
		elif animal == "cat":
			self.cat_q.append([animal,self.time_stamp])
		else:
			print "error : invalid animal"

	def de_q(self,animal=None):
		if animal is None and len(self.dog_q) + len(self.cat_q) > 0:
			if len(self.dog_q) == 0:
				return self.cat_q.popleft()
			if len(self.cat_q) == 0:
				return self.dog_q.popleft()
			if self.cat_q[0][1] < self.dog_q[0][1]:
				return self.cat_q.popleft()
			return self.dog_q.popleft()
		if animal == "dog" and len(self.dog_q) > 0:
			return self.dog_q.popleft()
		if animal == "cat" and len(self.cat_q) > 0:
			return self.cat_q.popleft()
		return "invalid animal"	

a = AnimalQueue()
a.en_q("cat")
a.en_q("dog")
a.en_q("dog")
a.en_q("cat")
a.en_q("dog")
print a
print a.de_q()
print a.de_q()
print a.de_q()


print a.de_q()
print a
print a.de_q()
print "so far so good"
print a.de_q()

print a
print a.de_q("dog")
print a

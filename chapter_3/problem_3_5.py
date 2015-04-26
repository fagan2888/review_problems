class MyQueue(object):
	
	def __init__(self):
		self.q = []
		self.dq = []

	def push(self,value):
		self.q.append(value)
	
	def pop(self):
		self.pour_q(self.q,self.dq)
		v = self.dq.pop()
		self.pour_q(self.dq,self.q)
		return v

	def pour_q(self,q1,q2):
		while q1:
			q2.append(q1.pop())	

m = MyQueue()
m.push(2)
m.push(3)
m.push(4)
m.push(5)
m.push(6)
print m.pop()
print m.pop()

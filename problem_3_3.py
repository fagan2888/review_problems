class SetOfStacks(object):

	def __init__(self,mx):
		self.mx = mx
		self.curr_stack = 0 
		self.stacks = [[]]
		self.idx = None

	def __str__(self):
		return str(self.stacks)

	def push(self,val):
		self.idx = 0 if self.idx is None else self.idx + 1
		if len(self.stacks[self.curr_stack]) == self.mx:
			self.stacks.append([val])
			self.curr_stack += 1
		else:
			self.stacks[self.curr_stack].append(val)

	def pop(self,pos=None):
		if pos is None:
			pos = self.idx
		if self.idx is None or pos > self.idx:
			return "out of range"
		if pos == self.idx:
			v = self.stacks[self.curr_stack].pop()
			if (pos + 1) % self.mx == 1 and pos != 0:
				self.stacks.pop()
				self.curr_stack -= 1
			if self.idx > 0:
				self.idx -= 1
			else: 
				self.idx = None
		return v
		
s = SetOfStacks(3)
print s
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(7)
s.push(8)
s.push(9)
s.push(10)
s.push(11)
print s
print s.pop()
print s
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s
s.push(0)
print s
s.push(1)
print s

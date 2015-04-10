class ArrayStack(object):
	
	def __init__(self,sub_size=10,sub_arrays=3):
		self.sub_arrays = sub_arrays
		self.sub_size = sub_size
		self.size = self.sub_arrays * self.sub_size
		self.array = [None] * self.size
		self.pointer = [i * self.sub_size for i in range(self.sub_arrays)]
		self.lower_bound = self.pointer[:]
		self.upper_bound = [x + (self.sub_size - 1) for x in self.pointer]

	def __str__(self):
		return str(self.array)

	def push(self,stack,value):
		stack_idx = stack - 1
		if self.pointer[stack_idx] > self.upper_bound[stack_idx]:
			print "out of range for stack"
		else:
			p = self.pointer[stack_idx]
			self.array[p] = value
			self.pointer[stack_idx] += 1
			
	def pop(self,stack):	
		stack_idx = stack - 1d
		idx = self.pointer[stack_idx] - 1
		if idx >= self.lower_bound[stack_idx]:
			val,self.array[idx] = self.array[idx], None
			self.pointer[stack_idx] -= 1
			return val		else:
			return "out of range for stack"

a = ArrayStack(2,4)
print a
a.push(2,0)
a.push(2,0)
a.pop(2)
a.pop(2)
a.pop(2)
print a.pop(1)
a.push(1,0)
a.push(1,0)
a.pop(1)
print a
a.push(4,1)
a.push(4,2)
a.push(4,3)
print a.pop(4)
a.pop(1)
print a.pop(1)
a.push(4,44)
print a

"""
print a.pop(2)
a.push(2,0)
print a
a.push(2,1)
print a
a.push(2,2)
print a
a.push(2,3)
print a
a.push(2,4)
print a

print a.pop(2)
print a
print a.pop(2)
print a
print a.pop(2)
print a.pop(2)
print a.pop(2)
print a.pop(2)
a.push(2,0)
print a
a.push(1,0)
print a.pop(1)
print a.pop(1)
print a.pop(1)
#a.push(4,7)
print a
"""

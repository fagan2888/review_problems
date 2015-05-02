class Node(object):
	def __init__(self,value):
		self.value = value
		self.next = None
		
class LinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None
	def push(self,value):
		node = Node(value) 
		if self.head is None:
			self.head = node
			self.tail = node
		self.tail.next = node
		self.tail = node
	def __str__(self):
		if self.head is None:
			return 'No items in list'
		node = self.head
		linked_list = []
		while node is not None:
			linked_list.append(str(node.value))
			node = node.next
		linked_list = ' -> '.join(linked_list)
		return linked_list
	def reverse(self):
		if self.head is not None:
			prev = self.head
			self.tail = prev
			curr = prev.next
			prev.next = None
			while curr is not None:
				nxt = curr.next
				curr.next = prev
				prev = curr
				curr = nxt
			self.head = prev
				
l = LinkedList()
l.push(11)
l.push(22)
l.push(33)
l.push(44)
l.push(55)

print l
l.reverse()
print l

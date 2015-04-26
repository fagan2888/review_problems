class Node(object):
	def __init__(self,value):
		self.value = value
		self.next = None
	def __str__(self):
		return str(self.value)

class LinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None
	def addNode(self,value):
		node = Node(value)
		if self.head is None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node
	def fromList(self,values):
		for value in values:
			self.addNode(value)
	def toList(self):
		if self.head is not None:
			index = self.head
			vector = [index.value]
			while index.next:
				index = index.next
				vector.append(index.value)
			return vector
	def __str__(self):
		if self.head is not None:
			index = self.head
			nodestore = [str(index.value)]
			while index.next != None:
				index = index.next
				nodestore.append(str(index.value))
			return "LinkedList [ " + "->".join(nodestore) + " ]"
		return "LinkedList []"

linkedlist = LinkedList()
values = [1,2,3,4,5,3,2,4,6]
linkedlist.fromList(values)

#print linkedlist
#print linkedlist.toList()

def remove_dupes(ll):
	if ll.head is not None:
		n = ll.head
		dc = {n.value : True}
		while n.next is not None:
			if n.next.value in dc:
				if n.next.next is not None:
					n.next = n.next.next
				else:
					n.next = None
			else:
				dc[n.value] = True
				n = n.next

# 2.1a remove_dupes(linkedlist)

def r_dupes(ll):
	if ll.head is not None:
		n = ll.head
		while n is not None:
			r = n
			while r.next is not None:
				if n.value == r.next.value:
					r.next = r.next.next
				else:
					r = r.next
			n = n.next

#2.1b r_dupes(linkedlist)

def rm_node(ll,n):
	if n.next is not None:
		n.value = n.next.value
		n.next = n.next.next
	else:
		n.value = None

n = linkedlist.head.next.next.next

#2.3 rm_node(linkedlist,n)

def ex_n(ll):
	if ll.head is not None:
		n = ll.head
		v = n.value
		m = 1
		while n.next is not None:
			m = m * 10
			v = v + m * n.next.value
			n = n.next
	else:
		v = 0
	return v

def add_lls(l1,l2):
	v = ex_n(l1) + ex_n(l2)
	l = LinkedList()
	for e in str(v)[::-1]:
		l.addNode(e)
	return l



l1 = LinkedList()
l1.fromList([7,1,6])
l2 = LinkedList()
l2.fromList([5,9,2])

#2.5a print add_lls(l1,l2)

def rev(ll):
	if ll.head is not None:
		curr = ll.head
		prev = None
		while curr is not None:
			nxt = curr.next
			curr.next = prev
			prev = curr
			curr = nxt
		ll.head = prev
	
rev(l2)
print l2
		
		


#print linkedlist





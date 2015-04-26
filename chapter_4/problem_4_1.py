from abstract_data_types.BinaryTree import *

t = BinarySearchTree()

l = [70,31,93,94,14,23,73]
for i in l:
    t.push(i)
print t

print t.root
print t.root.right.right
print t.root.left.right
print t.depth

print t

print t.find_value(15,t.root)

print t.get_height(t.root.left)
print t.get_height(t.root.right)
print t.is_balanced()
t.push(24)
print t.is_balanced()

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
s = BinarySearchTree()



def get_bst_list(l,z):
	if len(l) == 1:
		p = l.pop()
		z.append(p)
		return z
	h = len(l)/2
	h1 = l[:h]
	h2 = l[h:]
	if h2:
		z.append(h2.pop(0))
		if h2:
			z = get_bst_list(h2,z)
	if h1:
		z = get_bst_list(h1,z)
	return z

z = []
z = get_bst_list(l,z)
#print z

for e in z:
	s.push(e)


def is_bst(parent):
	if parent is None:
		return True
	if parent.left is not None:
		if parent.left.value >= parent.value:
			return False
		if not is_bst(parent.left):

			return False
	if parent.right is not None:
		if parent.right.value <= parent.value:

			return False
		if not is_bst(parent.right):

			return False
	return True
print s
print is_bst(s.root)
j = BinarySearchTree()
j.push(5)
print j.root.value

print j
print is_bst(j.root)

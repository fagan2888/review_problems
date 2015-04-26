from abstract_data_types.BinaryTree import *


t = BinarySearchTree()
l = [8,4,12,2,6,10,14,1,3,5,7,9,11,13,15]
for i in l:
	t.push(i)
print t
#paths = set()
def get_path(n, v, c=0,p='S',paths=set()):
	if n is None: return
	if c + n.value == v: paths.add(p)
	get_path(n.left, v, c + n.value,p + '->L',paths)
	get_path(n.right, v, c + n.value,p + '->R',paths)
	return paths
paths = get_path(t.root,30)


print paths

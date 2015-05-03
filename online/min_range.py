def get_range_dict(seqs,mn,mx):
	d = {}
	for i in range(mn,mx+1):
		d[i] = {-1}	 
	for i,seq in enumerate(seqs):
		for e in seq:
			if d[e] == {-1}:
				d[e] = {i}
			else:
				d[e].add(i)
	return d
					

def min_range(seqs):
	magic_number = len(seqs)
	mx = []
	mn = []
	for seq in seqs:
		mn.append(seq[0])
		mx.append(seq[-1])
	mn = min(mn)
	mx = max(mx)
	d = get_range_dict(seqs,mn,mx)
	r = range(mn,mx + 1)
	for i in range(1,len(r) + 1): 
		for j in r:
			sets = []
			for k in range(i):
				if j + k < mx + 1:
					for e in d[j + k]:
						if e != -1:
							sets.append(e)
					if len(sets) == magic_number:
						return i
					
l1=[4, 10, 15, 24, 26,31]
l2=[0, 9, 12, 20]
l3=[5, 18, 22, 30]

l1 = [1]
l2 = [5]
l3 = [2]
"""
def to_prev(seqs):
	mx = 0
	for seq in seqs:
"""		


#print min_range([l1,l2,l3])
 

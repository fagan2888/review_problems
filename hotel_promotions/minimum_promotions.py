#!/usr/bin/env python 

def ch(n,r):
	if r == 0:
		return 1
	mx = max(r,n-r)
	mn = min(r,n-r)
	i = 0
	nm = 1
	while i < mn:
		nm = (n - i) * nm
		i += 1
	i = 1
	dm = 1
	while i <= mn:
		dm = i * dm
		i += 1
	return nm/dm

def get_combinations(seq,prev,stop):
	c = []
	for e in prev:
		for i in seq:
			if i not in e:
				s = e + [i]
				s.sort()
				if s not in c:
					c.append(s)
				if len(c) == stop:
					return c
 	
def combination_ladder(seq,prev=[]):
	z = []
	if prev == []:
		for s in seq:
			z.append([s])
		return z
	seq_len = len(seq)
	p_lev = len(prev[0])
	lev = p_lev + 1
	return get_combinations(seq,prev,ch(seq_len,lev))

def get_reservation_dict(checkin,checkout):
	r = {}
	for i in range(len(checkin)):
		r[i] = {'check_in':checkin[i],'check_out':checkout[i]}
	return r

def guest_overlap(guest1,guest2):
	g1 = range(guest1['check_in'],guest1['check_out'] + 1)
	g2 = range(guest2['check_in'],guest2['check_out'] + 1)
	for i in g1:
		if i in g2:
			return True
	return False

def get_adjecent(res_dict):
	adj_list = {}
	for guest in res_dict:
		adj_list[guest] = []
		for other in res_dict:
			if guest != other:
				if guest_overlap(res_dict[guest],res_dict[other]):
					adj_list[guest].append(other)
	return adj_list

def min_promotions(guests,res_dict,adj_list,past_level):
	good_rev = []
	cs = combination_ladder(guests,past_level)
	for c in cs:
		for g in c:
			good_rev.append(g)
			for e in adj_list[g]:
				good_rev.append(e)
			if set(good_rev) == guests:
				return {'minimum promotions':len(c),'possible configuration':c}
		good_rev = []
	return min_promotions(guests,res_dict,adj_list,cs)

#checkin = [1,3,5,7,10,11,12]
#checkout = [4,4,7,8,12,13,13]

def get_min_promotions(checkin,checkout):
	guests = range(len(checkin))
	guests = set(guests)
	res_dict = get_reservation_dict(checkin,checkout)
	adj_list = get_adjecent(res_dict)
	return min_promotions(guests,res_dict,adj_list,[])

checkin = [1,3,5,7]
checkout = [2,4,7,8]

#print get_min_promotions(checkin,checkout)

checkin = [2,10,6]
checkout = [6,11,9]

#print get_min_promotions(checkin,checkout) # returns 2

checkin = [2, 10, 23, 34, 45, 123, 1]
checkout = [25, 12, 40, 50, 48, 187, 365]

#print get_min_promotions(checkin,checkout) # returns 1

checkin = [8, 12, 20, 30, 54, 54, 68, 75]
checkout = [13, 31, 30, 53, 55, 70, 80, 76]

#print get_min_promotions(checkin,checkout) # returns 3

checkin = [124, 328, 135, 234, 347, 124, 39, 99, 116, 148]
checkout = [237, 335, 146, 246, 353, 213, 197, 215, 334, 223]

#print get_min_promotions(checkin,checkout) # returns 2

checkin = [154, 1, 340, 111, 92, 237, 170, 113, 241, 91, 228, 134, 191, 86, 59, 115, 277, 328, 12, 6]
checkout = [159, 4, 341, 118, 101, 244, 177, 123, 244, 96, 231, 136, 193, 95, 64, 118, 282, 330, 17, 13]

checkin = [154, 1, 340, 111, 92, 237, 170, 113, 241, 91, 228, 134, 191, 86, 59]
checkout = [159, 4, 341, 118, 101, 244, 177, 123, 244, 96, 231, 136, 193, 95, 64]

print get_min_promotions(checkin,checkout) # too slow




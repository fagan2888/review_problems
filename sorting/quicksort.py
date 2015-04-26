#!/usr/bin/env python

def quicksort(l):
	if l == []:
		return []
	else:
		pivot = l[0]
		lesser = quicksort([x for x in l[1:] if x < pivot])
		greater = quicksort([x for x in l[1:] if x >= pivot])
		return lesser + [pivot] + greater

lst = [33,6,43,32,63,66,3,45,8,201,98,78,98,23,43,12,36,72]

print quicksort(lst)

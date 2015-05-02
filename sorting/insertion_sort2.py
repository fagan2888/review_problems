#!/usr/bin/env python

def insertion_sort(seq):
    for i in range(len(seq)):
		print i , 'time'
		j = i
		while j > 0 and seq[j - 1] > seq[j]:
			print 'seq[',j-1,'],seq[',j,'] = seq[',j,'], seq[',j-1,']' 
			seq[j-1],seq[j] = seq[j],seq[j-1]
			print seq
			j -= 1
    return seq

seq = [33,6,43,32,63,66,3,45,8,201,98,78,98,23,43,12,36,72,17,1]
seq = [2,3,1,5,4]
print seq
print insertion_sort(seq)

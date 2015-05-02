#!/usr/bin/env python

def quicksort(seq,start=0,pivot=None):
	if pivot is None:
		pivot = len(seq) - 1 #set final index as pivot
	if pivot - start <= 0:
		return #stop if sorting only one element
	wall = start
	for i in range(start,pivot + 1):
		if seq[i] < seq[pivot]:
			seq[wall],seq[i] = seq[i],seq[wall] #swap wall and index
			wall += 1 #increment wall
	seq[wall],seq[pivot] = seq[pivot],seq[wall] #swap the wall and pivot
	quicksort(seq,start,wall - 1) #recursively sort list up to pivot
	quicksort(seq,wall,pivot) #recursively sort list after pivot

seq = [6,2,1,3,8,4,7,9,5]
quicksort(seq)
print seq

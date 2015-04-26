#!/usr/bin/env python

def insertion_sort(lst):
    for i in range(len(lst)):
        j = i
        while j > 0 and lst[j - 1] > lst[j]:
            lst[j-1],lst[j] = lst[j],lst[j-1]
            j -= 1
    return lst

lst = [33,6,43,32,63,66,3,45,8,201,98,78,98,23,43,12,36,72,17,1]

print insertion_sort(lst)




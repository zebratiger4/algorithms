# -*- coding: utf-8 -*-
"""
Created on Mon May  7 16:27:19 2018

@author: Mike
"""


import numpy as np


def quicksort(A):
       n = A.shape[0]
       if n>1:
              i,cnt = partition_final(A,0,n)
              cnt1 = quicksort(A[0:i])
              cnt2 = quicksort(A[(i+1):n])
       else:
              cnt1,cnt2,cnt = 0,0,0
              
       return (cnt + cnt1+cnt2)


def partition(A,l,r):
       cnt = 0
       p = A[l]
       i = l + 1
       for j in range(l+1,r,1):
              if A[j]<p:
                     A[i],A[j] = A[j],A[i]
                     i = i + 1
              cnt = cnt + 1
       A[i-1],A[l] = A[l],A[i-1]

       return i-1,cnt

def partition_final(A,l,r):
       cnt = 0
       p = A[r-1]
       i = l
       for j in range(l,r-1,1):
              if A[j]<p:
                     A[i],A[j] = A[j],A[i]
                     i = i + 1
              cnt = cnt + 1
       A[i-1],A[r-1] = A[r-1],A[i-1]

       return i-1,cnt       


# Test case
z = np.array([3,2,1])
quicksort(z)


######
# To handle the case in homework
text_file = open("QuickSort.txt","r")
lines = text_file.readlines()


z = [line.split('\n') for line in lines]
arr = np.array([int(e[0]) for e in z])



quicksort(arr)
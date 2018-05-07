# -*- coding: utf-8 -*-
"""
Created on Fri May  4 19:16:32 2018

@author: A
"""


import numpy as np


# define a function to count the # of inversions in the split case 
def merge_split_cnt(A,B):
       
       n1 = A.shape[0]
       n2 = B.shape[0]
       
       i,j = 0,0
       split_cnt = 0
       
       for k in range(n1+n2):
              if (i<n1) and (A[min(i,n1-1)]<B[min(j,n2-1)]):
                     i = i + 1
              elif (j<n2) and (A[min(i,n1-1)]>=B[min(j,n2-1)]):
                     j = j + 1
                     split_cnt = split_cnt + n1 - i
                     
       return split_cnt



# define a function to count the # of inversions
def count_split(A):
       n = A.shape[0]
       if n == 1:
              return 0
       
       mid = int(n/2)
       x = count_split(A[0:mid])
       C = np.sort(A[0:mid])
       y = count_split(A[mid:n])
       D = np.sort(A[mid:n])
       z = merge_split_cnt(C,D)

       return x+y+z


#######
# Some text case
z= np.array([2,3,1,5,4])
count_split(z)
#######


######
# To handle the case in homework
text_file = open("IntegerArray.txt","r")
lines = text_file.readlines()


z = [line.split('\n') for line in lines]
arr = np.array([int(e[0]) for e in z])

count_split(arr)



# -*- coding: utf-8 -*-
"""
Created on Wed May  9 10:26:09 2018

@author: A
"""

import numpy as np
import random



# Functions for random contraction algorithms
def rand_contraction(graph):
       V = list(graph.keys())
       while len(V)>2:
              v = random.choice(V)
              u = random.choice(graph[v])
              graph[v] = graph[u] + graph[v]
              while u in graph[v]:
                     graph[v].remove(u)
              while v in graph[v]:
                     graph[v].remove(v)
              for vex in V:
                     if (u in graph[vex]) and vex!=v:
                            while u in graph[vex]:
                                   graph[vex].remove(u)
                                   graph[vex].append(v)
              del graph[u]
              V = list(graph.keys())
       return len(graph[V[0]])
              
         
     
       
######
# To handle the case in homework
text_file = open("kargerMinCut.txt","r")
lines = text_file.readlines()

edges = [line.split('\n') for line in lines]
edgs = [edge[0].split('\t')[:-1] for edge in edges]


# Convert it to dictionary
graph = {}
for edg in edgs:
       graph[edg[0]] = edg[1:]


n = len(graph.keys())
res = []

for i in range(100):
       # Convert it to dictionary
       graph = {}
       for edg in edgs:
              graph[edg[0]] = edg[1:]
       res.append(rand_contraction(graph))
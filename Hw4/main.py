# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:58:52 2018

@author: Mike
"""

import numpy as np
from collections import defaultdict



# define a graph class to store graph
class Graph:
       
       def __init__(self,vertices):
              self.V = vertices
              self.graph = defaultdict(list)
              
       
       def addEdge(self,u,v):
              self.graph[u].append(v)
              
              
              
       # Get reverse graph
       def reverse(self):
              g = Graph(self.V)
              
              for i in self.graph:
                     for j in self.graph[i]:
                            g.addEdge(j,i)
                            
              return g



       
       def addTag(self,v,visited,stack):
              visited[v] = True
              for i in self.graph[v]:
                     if visited[i] == False:
                            self.addTag(i,visited,stack)
              stack.append(v)
       


       def DFS_loop(self,v,visited,leader,leader_node):
              visited[v] = True
              leader[v] = leader_node
              for i in self.graph[v]:
                     if visited[i] == False:
                            self.DFS_loop(i,visited)
       
       
       def SCCs(self):
              stack = []
              leader = [0] * self.V
              visited = [False] * (self.V)
              
              # Add the order to the original node
              for i in self.graph:
                     if visited[i] == False:
                            self.addTag(i,visited,stack)
                            
              graph_rev = self.reverse()
              
              visited = [False] * (self.V)
              
              while stack:
                     i = stack.pop()
                     if visited[i] ==  False:
                            leader_node = i
                            graph_rev.addTag(self,)





       
######
# To handle the case in homework
text_file = open("SCC.txt","r")
lines = text_file.readlines()


edges = [line.split(' ') for line in lines]


vertices = [int(edge[0]) for edge in edges]
numV = len(np.unique(vertices))


graph = Graph(875715)
for edge in edges:
       graph.addEdge(int(edge[0]),int(edge[1]))








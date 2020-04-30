# -*- coding: utf-8 -*-
import math

class Graph:
    def __init__(self, vertices):
        self.Nv = len(vertices)
        self.V = vertices
        self.graph = []
        self.fillGraph(vertices)
        self.result = []
        
    # function to fill the graph
    def fillGraph(self, vertices):
        for i in range(0,self.Nv):
            for j in range(i,self.Nv):
                if i != j:
                    w = self.getWeights(vertices[i], vertices[j])
                    self.graph.append([i,j,w])
        # sorting the graph
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
    
    # Euclidean distance 
    def getWeights(self, u, v):
        d = math.sqrt((u[0]-v[0])**2 + (u[1]-v[1])**2)
        return d
    
    # find the parent
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i])
    
    # updating parent and rank info
    def update(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 

        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 
  
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1
    
    # finding the MST
    def getMST(self):
        result = []
        
        # index of all the vertices
        gIndex = 0
        # index of added vertices
        rIndex = 0
        
        parent = []
        rank = []
        
        for node in range(self.Nv): 
            parent.append(node) 
            rank.append(0) 
        
        while rIndex < self.Nv -1 : 
            u,v,w =  self.graph[gIndex] 
            gIndex = gIndex + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 
            
            # add if it does not form a loop
            if x != y: 
                rIndex = rIndex + 1     
                result.append([u,v,w])
                # adding new edge info for parent information
                self.update(parent, rank, x, y)
        # final result list with edge info
        self.result = result
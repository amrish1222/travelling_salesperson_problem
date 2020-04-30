# -*- coding: utf-8 -*-
import tsplib95 as tsp
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import time

from graph import Graph as gc
from DFS import Dfs
from heuristic import Heuristic

# to get the distace between points to calculate cost
def getWeights(u, v):
    d = math.sqrt((u[0]-v[0])**2 + (u[1]-v[1])**2)
    return d

start_time = time.time()

# import the .tsp file
TSP = tsp.utils.load_problem("eil51.tsp")
V = len(list(TSP.get_nodes()))
E = list(TSP.get_edges())

# required number of edges = V-1
N_e = V-1

vertices = []

# get the vertices from file using the library
for i in range(1,V+1):
    # add vertices to a list
        vertices.append(TSP.node_coords[i])

# initialize an instance of graph class
prob = gc(vertices)

# get MST usign the class function
prob.getMST()

# get only required vertice information
mst = np.array(prob.result)[:,[0,1]]

mst = mst.astype(int)

# Plot MST to view
verticesArr = np.array(vertices)
xI = [0,0]
yI = [0,0]

plt.figure(1)
for i in range(0, len(mst)):
    xI[0] = verticesArr[mst[i,0]][0]
    xI[1] = verticesArr[mst[i,1]][0]
    yI[0] = verticesArr[mst[i,0]][1]
    yI[1] = verticesArr[mst[i,1]][1]
    
    plt.plot(xI, yI , 'ro-')

plt.show()

# Calculate cost of MST
cost = np.array(prob.result)[:,[2]]
print("Cost of MST = ", np.sum(cost))

# DFS to get tour
edges = np.array(prob.result)[:,[0,1]].astype(int)

# initialize instance of DFS class
dfs = Dfs(edges)

# Arbitrary starting vertex
startVer = random.randint(0,len(vertices))

# run the recurssive function to get tour using dfs
dfs.recurssiveFunc(startVer)

print("Starting Vertex", startVer)

# get tour from class variable
dfsTour = dfs.tour

# get tour after adding shortcuts
shortcutTour = dfs.getShortcut(dfsTour)

# plot tour after shortcuts
plt.figure(2)
tourCost = 0
for i in range(0,len(shortcutTour)-1):
    
    xI[0] = verticesArr[shortcutTour[i]][0]
    xI[1] = verticesArr[shortcutTour[i+1]][0]
    yI[0] = verticesArr[shortcutTour[i]][1]
    yI[1] = verticesArr[shortcutTour[i+1]][1]
    
    tourCost += getWeights(verticesArr[shortcutTour[i]],verticesArr[shortcutTour[i+1]])
    plt.plot(xI, yI , 'yo-', alpha = 0.5, lw = 4)
    txt = str(shortcutTour[i])
    plt.annotate(txt,(xI[0],yI[0]))   
plt.show()

# get cost after adding shortcuts
tourCost = int(tourCost)
print("Tour Cost after shortcut= ", tourCost)

# initialize an instance of the heuristic class
heur = Heuristic(shortcutTour, vertices)

# Iterate through all the points and fix intersections
heur.iterateAndFix()

# iterate once more to make sure all intersections are resolved
heur.iterateAndFix()

# get the required tour
tour = heur.tour
# print the tour
print(tour)

# plot the final tour
plt.figure(3)
tourCost = 0
for i in range(0,len(tour)-1):
    
    xI[0] = verticesArr[tour[i]][0]
    xI[1] = verticesArr[tour[i+1]][0]
    yI[0] = verticesArr[tour[i]][1]
    yI[1] = verticesArr[tour[i+1]][1]
    
    tourCost += getWeights(verticesArr[tour[i]],verticesArr[tour[i+1]])
    plt.plot(xI, yI , 'go-', alpha = 0.5, lw = 4)
    txt = str(tour[i])
    plt.annotate(txt,(xI[0],yI[0]))   
plt.show()
tourCost = int(tourCost)
print("Tour Cost after heuristic= ", tourCost)
end_time = time.time()
print("Total time taken to run the algorithm(seconds): ", end_time-start_time)


# output the required file
def file_out(filename,tour_length,finalTour):
	f=open(f'{filename}.out.tour','w+')
	f.write(f"NAME : {filename}.out.tour\n")
	f.write(f'COMMENT : Tour for {filename}.tsp (Length {tour_length})\n')
	f.write(f'TYPE : TOUR\n')
	f.write(f'DIMENSION : {len(finalTour)-1}\n')
	f.write(f'TOUR_SECTION\n')
	for i in range(0,len(tour)):
		f.write(f'{finalTour[i]}\n')
	f.write(f'-1\n')
	f.write(f'EOF')
file_out("eil51",tourCost,tour)



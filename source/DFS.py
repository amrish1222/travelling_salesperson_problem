# -*- coding: utf-8 -*-



class Dfs:
    def __init__(self, edges):
        self.edgesArr = edges
        self.remainEdgesIndx = list(range(0, len(edges)))
        self.tour = []
       
    # returns vertices in order using a recurssive function
    def recurssiveFunc(self, vertexIndx):
        # adding the current vertex
        self.tour.append(vertexIndx)
        terminate, nextEdges, nextVertices = self.nxtEdge_Vertices(vertexIndx)
        if terminate:
            pass
        else:
            for e,v in zip(nextEdges,nextVertices):
                if len(self.remainEdgesIndx) != 0:
                    self.remainEdgesIndx.remove(e)
                    self.recurssiveFunc(v)
                    # adding the previous vertex after going ahead and terminating
                    self.tour.append(vertexIndx)
                else:
                    pass
                
    # finding the next edge and vertex with the current one
    def nxtEdge_Vertices(self, vertexIndx):
        edge = []
        vertex = []
        for e in self.remainEdgesIndx:
            if vertexIndx == self.edgesArr[e,0]:
                edge.append(e)
                vertex.append(self.edgesArr[e,1])
            elif vertexIndx == self.edgesArr[e,1]:
                edge.append(e)
                vertex.append(self.edgesArr[e,0])
            else:
                pass
        if len(edge) == 0:
            return True, edge, vertex
        else:
            return False, edge, vertex
    
    # getting shortcut by removing repeated vertices  
    def getShortcut(self, dfsTour):
        finalTour = []
        visitedSet = set([])
        finalTour.append(dfsTour[0])
        visitedSet.add(dfsTour[0])
        for i in range(1,len(dfsTour)):
            if dfsTour[i] in visitedSet:
                pass
            else:
                finalTour.append(dfsTour[i])
                visitedSet.add(dfsTour[i])
        # adding the first vertex back to complete the tour
        finalTour.append(dfsTour[0])
        return finalTour
            
# -*- coding: utf-8 -*-


class Heuristic:
    def __init__(self, tour, vertices):
        self.tour = tour
        self.vertices = vertices
        self.newTour = tour
        
    # to check if points are in ccw order    
    def ccw(self, a, b, c):
        A = self.vertices[a]
        B = self.vertices[b]
        C = self.vertices[c]
        # angle of AB vs AC
        return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])
    
    # using the direction of points checking for intersection
    def intersect(self,a,b,c,d):
        return self.ccw(a,c,d) != self.ccw(b,c,d) and self.ccw(a,b,c) != self.ccw(a,b,d)
    
    def iterateAndFix(self):
        intersect = True
        # run until intersections stop
        while intersect:
            intersect = False
            for i in range(0,len(self.tour)-2):
                if intersect: break
                for j in range(i+2, len(self.tour)-1):
                    if self.intersect(self.tour[i],self.tour[i+1],self.tour[j],self.tour[j+1]):
                        # fix the intersection
                        intersect = True
                        self.fixIntersection(i,i+1,j,j+1)
                        break
                    else:
                        pass
            # once the intersection is fixed update the tour with the copy
            self.tour = self.newTour
    
    # everytime an intersection is seen between two edges the tour has to be
    # modified by flipping the whole between the edges which will fix the intersection
    def fixIntersection(self, p, q, r,s):
        # stores the path between the edges
        storePath = self.newTour[q:r+1]
        # flip the stored path
        storePath.reverse()
        # add it back to copy of the tour
        self.newTour[q:r+1] = storePath[:]
        
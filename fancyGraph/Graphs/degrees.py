# -*- coding: utf-8 -*-
from fancyGraph.Vertex import Vertex
from fancyGraph import PreProcess
from fancyGraph.FancyGraph import FancyGraph

class graphs(Vertex):
    def __init__(self, ID, value, neighbors):
        Vertex.__init__(self, ID, value, neighbors)
        self.deg = len(neighbors)
        
    def update(self):
        pass

"""
This method returns list of objects of vertex.
You may also want to initialize the value of each vertex,
which can be achived by passing a argument value.
"""
def generateGraph(path, value=0):
    array_list = PreProcess.readFile(path)
    vertices = []
    for i in range(len(array_list)):
        vertex = graphs(i, value, array_list[i])
        vertices.append(vertex)
    return vertices        
        
def deg():
    path = "../../graphData/testGraph.txt"
    vertices = generateGraph(path)
    alg = FancyGraph(vertices,-1)
    alg.superstep()
    return [vertex.deg for vertex in alg.vertices]

print (deg())

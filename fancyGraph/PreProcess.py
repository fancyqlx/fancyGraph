# -*- coding: utf-8 -*-

"""
We prefer to address the txt file containing data as the format [src des]
"""
def readFile(path):
    f = open(path,'r')
    array_list = []
    for line in f:
        src, des = map(int,line.split())
        if len(array_list)-1 < src:
            array_list.append([])
        array_list[src].append(des)
    return array_list
    

#"""
#This method returns list of objects of vertex.
#You may also want to initialize the value of each vertex,
#which can be achived by passing a argument value.
#"""
#def generateGraph(path, value=0):
#    array_list = readFile(path)
#    vertices = []
#    for i in range(len(array_list)):
#        vertex = Vertex(i,value,array_list[i])
#        vertices.append(vertex)
#    return vertices
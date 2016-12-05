# -*- coding: utf-8 -*-
import threading

class Vertex(threading.Thread):
    def __init__(self,id,value,out_vertices):
        threading.Thread.__init__(self)
        self.id = id
        self.value = value
        self.out_vertices = out_vertices
        self.incoming_messages = []
        self.outgoing_messages = []
        self.active = True
        self.superstep = 0

    def run(self):
        self.update()

    def update(self):
        """A method for user to override: update the vertex's value"""
        pass
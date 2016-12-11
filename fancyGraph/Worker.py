# -*- coding: utf-8 -*-
import threading

"""
Worker is a class that inherits thread to simulate a processor, i.e., a vertex.
"""

class Worker(threading.Thread):
    def __init__(self, vertex, barrier):
        threading.Thread.__init__(self)
        self.vertex = vertex
        self.flag = True
        self.barrier = barrier
        
    """
    A method that overrides run() in Thread.
    self.barrier.wait() is used for synchronizing threads,
    i.e., a superstep. The thread is released if and only if 
    all the workers called this function wait().
    """
    def run(self):
        while self.flag:
            self.barrier.wait()
            print (self.getName())
            if self.vertex.active:
                self.vertex.update()
            
    def isTerminated(self,flag):
        self.flag = flag
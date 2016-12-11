# -*- coding: utf-8 -*-
import threading
from fancyGraph.Worker import Worker

"""
A logic class for scheduling the threads.

Note that we set argument 'rounds', rounds == -1 means
there is no limit on rounds of algorithms.
"""

class FancyGraph():
    def __init__(self, vertices, rounds):
        self.vertices = vertices
        self.num_workers = len(vertices)
        self.rounds = rounds
        self.limit = (rounds == -1)
        self.count = 0
        self.flag = True
        
    """
    Main method that simulate the messages passing.
    Using threading.Barrier() to synchronize all the threads.
    If there is no message delivered in the graph,
    or supersteps are at the limit, we finish the algorithm
    and join all the threads.
    
    Note that in the while loop, the barrier waits for
    all the worker of finishing the current superstep, then
    the self.count increases.
    
    Here we do not process vertex.outgoing_messages, since 
    we believe it is better for users to design algorithm
    according to vertex.update() method.
    """
    def superstep(self):
        workers = []
        barrier = threading.Barrier(self.num_workers+1)
        for vertex in self.vertices:
            worker = Worker(vertex, barrier)
            workers.append(worker)
            worker.start()
            
        while self.flag:
            barrier.wait()
            self.distributeMessages()
            self.count += 1
            print ("superstep: ", self.count)
            self.flag = self.isTerminated()
            
        for worker in workers:
            worker.isTerminated(self.flag)
            
        for worker in workers:
            worker.join()
        
    def distributeMessages(self):
        for vertex in self.vertices:
            vertex.incoming_messages = []
            if len(vertex.outgoing_messages) == 0: vertex.active = False
            for msg in vertex.outgoing_messages:
                des = msg[0]
                data = msg[1]
                self.vertices[des].incoming_messages.append((vertex.ID,data))
                self.vertices[des].active = True
                
    def isTerminated(self):
        return any([vertex.active for vertex in self.vertices]) and (self.limit or self.count < self.rounds)
        
    def output(self):
        pass
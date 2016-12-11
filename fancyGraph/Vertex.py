# -*- coding: utf-8 -*-
"""
Class for a vertex, handled by a thread, 
that is, a vertex is a memory address accessed by thead.
A vertex is regarded as a processer in a distributed algorithm.
Thus, all operations need to be defined in this class.
----------------------------------------
def __init__()
id: identity of a vertex
value: user defined
neighbors: a list of neighbors
incoming_messages: a list of messages this vertex received
outgoing_messages: a list of messages this vertex is going to send
active: boolean value means the vertex is active or not
superstep: a counter used for synchron
----------------------------------------
"""
class Vertex():
    def __init__(self, ID, value, neighbors):
        self.ID = ID
        self.value = value
        self.neighbors = neighbors
        self.incoming_messages = []
        self.outgoing_messages = []
        self.active = True
        
    
    """
    A method for user to override: update the vertex's value.
    All the messages it needs are stored in incoming_messages,
    and it need to determine what messages should be loaded into outgoing_messages.
    """
    def update(self):
        pass
    
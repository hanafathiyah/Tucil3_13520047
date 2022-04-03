from operator import le

from bnb import count_g

class NodePuzzle:
    def __init__(self, node_number, info, parent, depth):
        self.node_number = node_number
        self.info = info
        self.parent = parent
        self.depth = depth # count f
        self.c = self.depth + count_g(self.info)
    

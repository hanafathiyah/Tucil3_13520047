from operator import le

#from bnb import count_g

class NodePuzzle:
    def __init__(self, info, parent = None, depth = 0, move = ""):
        self.info = info
        self.parent = parent
        self.move = move
        self.depth = depth
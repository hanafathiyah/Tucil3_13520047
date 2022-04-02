from operator import le

from bnb import count_g

class NodePuzzle:
    def __init__(self, info, up, right, down, left):
        self.info = info
        self.up = up
        self.right = right
        self.down = down
        self.left = left
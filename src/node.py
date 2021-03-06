# LiveNode = simpul hidup (in bahasa)

class LiveNode:
    def __init__(self, function):
        self.liveNode = []
        self.function = function

    def is_empty(self):
        return len(self.liveNode) == 0
    
    def get_first(self):
        return self.liveNode[0]

    def add_in(self, new_node):
        i = 0
        lower_than = False

        while (not lower_than and i < len(self.liveNode)):
            if(self.function(new_node, self.liveNode[i])):
                lower_than = True
            else:
                i += 1
        
        self.liveNode.insert(i, new_node)
    
    def delete_first(self):
        self.liveNode.pop(0)
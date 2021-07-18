class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None
    

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def traverse(self, start_point=None):
        if start_point is None:
            start_point = self.head
        node = start_point
        while node is not None and (node.next != start_point):
            yield node
            node = node.next
        yield node
    
    def print_list(self, starting_point=None):
        nodes = []
        for node in self.traverse(starting_point):
            nodes.append(str(node))
        print(" -> ".join(nodes))

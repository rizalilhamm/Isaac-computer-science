from types import prepare_class

class Node:
    # Create Node to store data in linked list
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    # Create our own Linked List
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            # make sure the head of linked list is first element in linkedlist
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                # point to next data of linkedlist
                node.next = Node(data=elem)
                node = node.next


    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return " -> ".join(nodes)


    def __iter__(self):
        # This function used to show all data in linkedlist
        node = self.head
        while node is not None:
            yield node
            node = node.next


    def add_first(self, new_node):
        # add Node at the first of linked list
        new_node.next = self.head
        self.head = new_node


    def add_last(self, new_node):
        # Add new node add the last of linked list
        if self.head is None:
            # Set new node as head of linked list 
            self.head = new_node
            return
        # Traverse all linked list until the end 
        for current_node in self:
            pass
        # set new_node as next of current_node 
        current_node.next = new_node


    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is Empty")
        
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception("Targe with %s not found." % target_node_data)


    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is Empty")
        
        if self.head.data == target_node_data:
            return self.add_first(new_node)
        
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
        raise Exception("Targe with %s not found." % target_node_data)
                

    def remove_node(self, target_node_data):
        # Remove a Node from a linked list
        if self.head.data == None:
            raise Exception("List is Empty")
        
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        
        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)
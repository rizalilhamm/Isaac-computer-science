from typing import Annotated


class Queue:
    def __init__(self) -> list:
        self.items = []
        
    def __repr__(self):
        if len(self.items) < 1:
            return self.is_empty()
        return self.items

    def is_empty(self) -> bool:
        return self.items == []
    
    """
    def enqueu(self, data):
        # This is add at the last index
        self.items.append(data)
    """

    def enqueue(self, data):
        # insert new value at the first index
        self.items.insert(0, data)
    
    """
    def dequeue(self):
        # remove at the first index (index 0)
        return self.items.pop(0)
    """

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def print_data(self):
        data = [x for x in self.items]
        return data

if __name__ == '__main__':
    antri = Queue()
    print(antri.is_empty())
    antri.enqueue(10)
    print(antri.size())
    antri.enqueue(12)
    antri.enqueue(100)
    print(antri.is_empty())
    antri.dequeue()
    print(antri.print_data())
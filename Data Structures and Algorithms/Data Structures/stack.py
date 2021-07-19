class Stack:
    def __init__(self) -> list:
        self.stack = []

    def __repr__(self) -> list:
        if len(self.stack) <= 0:
            return 'Stack is empty'
        return self.stack
    
    def add(self, data):
        """Use list append to add at the end of stack"""
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False

    def peek(self):
        """Use peek to look at the top of Stack"""
        return self.stack[-1]
    
    def remove(self):
        if len(self.stack) <= 0:
            return 'Stack is empty'
        else:
            return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

if __name__ == '__main__':
    tumpukan = Stack()

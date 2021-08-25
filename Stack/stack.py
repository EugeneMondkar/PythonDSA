class Stack:
    
    dataContainer = list()
    
    def __init__(self) -> None:
        pass

    def push(self, item):
        self.dataContainer.append(item)
    
    def pop(self):
        return self.dataContainer.pop()

    def peek(self):
        return self.dataContainer[-1]

    def size(self):
        return len(self.dataContainer)

    def is_empty(self):
        if len(self.dataContainer) == 0:
            return True
        else:
            return False
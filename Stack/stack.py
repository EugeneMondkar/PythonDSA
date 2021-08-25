class Stack:
            
    def __init__(self) -> None:
        self.dataContainer = list()

    def push(self, item):
        self.dataContainer.append(item)
    
    def pop(self):
        return self.dataContainer.pop()

    def peek(self):
        return self.dataContainer[-1]

    def size(self):
        return len(self.dataContainer)

    def is_empty(self):
        return self.dataContainer == []
class Stack:

    def __init__(self, items=None, limit=100):
        if items is None:
            items = []
        self.items = items.copy()
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if not self.full(): 
            self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit  # >= for safety

    def search(self, target):
        try:
            return (len(self.items) - 1) - self.items.index(target)
        except ValueError:
            return -1
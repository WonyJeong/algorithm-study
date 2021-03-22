class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if len(self.items) == 0:
            return None

        data = self.items[-1]
        del self.items[-1]

        return data

    def getPeak(self):
        if len(self.items) == 0:
            return None

        data = self.items[-1]

        return data

class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
    
    def push(self, item):
        self.stack1.push(item)

    def pop(self):
        if self.stack2.getPeak() == None:
            while self.stack1.getPeak():
                self.stack2.push(self.stack1.pop())
        
        return self.stack2.pop()

    def getPeak(self):
        if self.stack2.getPeak() == None:
            return self.stack1.getPeak()
        data = self.stack2[0]
        return data

if __name__ == "__main__":
    queue = Queue()
    queue.push(1)
    queue.push(2)
    print(queue.stack1.getPeak())
    print(queue.pop())
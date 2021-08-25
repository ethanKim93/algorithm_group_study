class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        if len(self.queue):
            return -1
        return 1

    def enqueue(self, el):
        self.queue += [el]

    def dequeue(self):
        if self.queue:
            tmp = self.queue[0]
            self.queue = self.queue[1:]
            return tmp
        return -1

    # size
    def size(self):
        return len(self.queue)

myQueue = Queue()
myQueue.enqueue(1)
print(myQueue.queue)
myQueue.enqueue(2)
print(myQueue.queue)
myQueue.enqueue(3)
print(myQueue.queue)

print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
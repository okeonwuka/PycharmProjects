# Construct class

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def is_empty(self):
        return self.items == []

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


print("==================Test Queue ====================================================")

testQueue = Queue()
testQueue.enqueue('boy')
testQueue.enqueue('34')
testQueue.enqueue(677)
testQueue.enqueue('True')
testQueue.dequeue()  # you cant do testQueue.dequeue(34) becos dequeue takes no parameter.
#  Also because a queue is FIFO, testQueue.dequeque will remove the 'First Element/item' put  in the queue, which was boy
# If it was a stack, since it is LIFO pop() will remove the last item put in stack.
# Both pop() /dequeue() take no arguments and return Last/First item .


print(testQueue)

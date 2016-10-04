class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


print(
    "======================Stack Class Tests ===========================================================================")
URL = Stack()
URL.push('boy')
URL.push('34')
URL.push(677)
URL.push('True')

URL.push(498270984)
URL.pop()

print(URL)
print(URL.size())

print(
    "======================Exercises Pg 67 PSWAADS===========================================================================")

m = Stack()
m.push('x')
m.push('y')
m.push('z')

# while not m.is_empty():
#     m.pop()
#     m.pop()

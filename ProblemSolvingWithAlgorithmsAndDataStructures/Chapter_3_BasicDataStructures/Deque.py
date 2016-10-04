# Class constructor

class Deque:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        self.items.pop()

    def remove_rear(self):
        self.items.pop(0)

    def size(self):
        return len(self.items)


print(
    "======================Deque Class Tests ===========================================================================")

dequeTest = Deque()
print(dequeTest)
print(dequeTest.is_empty())

print(
    "======================Deque Class Tests: Fill her up from front! ===========================================================================")
print(dequeTest)
dequeTest.add_front('boy')
print(dequeTest)
dequeTest.add_front('34')
print(dequeTest)
dequeTest.add_front(677)
print(dequeTest)
dequeTest.add_front('True')
print(dequeTest)

print(
    "======================Deque Class Tests: Remove items from front! ( items in front have higher indexes than those in rear)=======================")
print(dequeTest)
dequeTest.remove_front()
print(dequeTest)
dequeTest.remove_front()
print(dequeTest)
dequeTest.remove_front()
print(dequeTest)
dequeTest.remove_front()
print(dequeTest)

print(
    "======================Deque Class Tests: Remove items from rear ( items in rear have lower indexes than those in front) ! =========================")
dequeTest.add_front('boy')
dequeTest.add_front('34')
dequeTest.add_front(677)
dequeTest.add_front('True')
# ==========================================================================
print(dequeTest)
dequeTest.remove_rear()
print(dequeTest)
dequeTest.remove_rear()
print(dequeTest)
dequeTest.remove_rear()
print(dequeTest)
dequeTest.remove_rear()
print(dequeTest)

print(
    "======================Deque Class Tests: Fill her up from rear ! ===========================================================================")
dequeTest = Deque()
print(dequeTest)
dequeTest.add_rear('boy')
print(dequeTest)
dequeTest.add_rear('34')
print(dequeTest)
dequeTest.add_rear(677)
print(dequeTest)
dequeTest.add_rear('True')
print(dequeTest)

class Speed(object):
    def __init__(self, d, t):
        self.distance = d
        self.time = t
        return d * t
        # def getspeedInHours(self):
        #     return
        #


# tesla = Speed(300,100)

class Node(object):
    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        return self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self, d):
        return self.data = d

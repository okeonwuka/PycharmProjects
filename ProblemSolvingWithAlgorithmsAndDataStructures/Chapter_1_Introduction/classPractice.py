# Car2 class ========================================================================

class Car1:
    def __init__(self, t, d):
        self.tyres = t
        self.doors = d

    @staticmethod  # @staticmethod  make it clear that this method should not receive the instance as the first parameter
    def make_car_sound():
        print("vrooooooom")


# Example instances of class Car1:
print("===================== Car1 tests =====================================")
BMW = Car1(4, 4)
BMW.make_car_sound()
print(BMW.doors)
print()


# Car2 class ========================================================================

class Car2:
    def __init__(self, t, d):
        self.tyres = t
        self.doors = d

    def __str__(self):
        return "This is Car2"


# Example instances of class Car2:
print("===================== Car2 tests =====================================")
Volvo = Car2(4, 4)
print(Volvo)


# Car2 class ========================================================================

class Car3:
    def __init__(self, t, d):
        self.tyres = t
        self.doors = d

    def __str__(self):
        return "This is Car3 has " + str(self.tyres) + " tyres and " + str(self.doors) + " doors"


# Example instances of class Car3:
print("===================== Car3 tests =====================================")
MackTruck = Car3(18, 6)
print(MackTruck)


# print(repr(MackTruck))




# Person class

class Person:
    def __init__(self, s, r):
        self.sex = s
        self.race = r

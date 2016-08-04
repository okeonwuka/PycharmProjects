class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.dem = bottom

    def __str__(self):
        return str(self.num) + '/' + str(self.dem)

    def __add__(self, other_fraction):
        new_num = self.num*other_fraction.dem + other_fraction.num*self.dem
        new_dem = self.dem + other_fraction.dem
        return Fraction(new_num, new_dem)
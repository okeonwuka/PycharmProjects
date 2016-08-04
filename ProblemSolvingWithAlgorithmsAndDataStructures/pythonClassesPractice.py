# Define class


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other_fraction):
        new_num = self.num*other_fraction.den + other_fraction.num*self.den
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)


# Test Fraction Class
quarter = Fraction(1, 4)
print(quarter)

half = Fraction(1, 2)
print(half)

# Test add method in fraction class
three_quarter = half + quarter
print(three_quarter)

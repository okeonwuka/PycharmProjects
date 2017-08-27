class Fraction:
    # This section, called the constructor method, creates the 'state' of the class
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    # This next section, generally called 'methods', defines how the class behaves ie its methods
    # This is actually the fun part. We get to customise everything about how this object acts. Everything has to be defined..how it prints out, adds, divides etc

    # Lets create a 'show' method for the class. This will allow the class object to print itself as a string
    def show(self):
        print(self.num, '/', self.den)

    # But its better to make the class work with the 'print' function in python. To do this, we need to use a method that will enable the class to
    # present itself as a string so that it can work with pythons print function. In python , all classes have a set of standard methods that are
    # provided. Examples of standard methods are __str__, __add__ etc. __str__ standard method serves to convert objects into strings. However, they
    # may not work properly with the classes we build, so must be modified to suit our class. See below
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    # Create method to add 2 fractions by repurposing standard method '__add__'
    # logic comes from mathematical addition of fractions(cross multiplication:
    # a/b + c/d = (ad+bc)/bd
    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)


    # Now we take care of getting the fractions to their lowest terms. To do this we need to find the "Greatest Common Divisor", GCD, between the denominator
    # and the numerator. Euclids algorithm helps with this. (Check algorithm in book, pg 34). a function that implements the algorithm is below:
    def gcd(m, n):
        while m % n !=0 :
            old_m = m
            old_n = n

            m = old_n
            n = old_m
        return n

# =============== function taken outside class to be globally recognised for testing purposes ====================================
def gcd(m, n):
        while m % n !=0:
            old_m = m
            old_n = n

            m = old_n
            n = old_m
        return n


print('=============================Test Code ============================================')

# To test our class, create actual instances of the class
print('Instantiate Fraction class:')
print('my_fraction = Fraction(5, 7)')
my_fraction = Fraction(5, 7)
print(' ')

# Execute show() method
print('Execute show method:')
# note:  print("my_fraction.show() ={}".format(my_fraction.show())) will 'none' coz 'my_fraction.show()' not built to handle  format function (i think)
my_fraction.show()
print(' ')

# Execute modified __str__ method (for proper use of pythons print function with our class)
print('Execute modified "__str__ method" (for proper use of pythons print function with our class)')
print('print(my_fraction) = {}'.format(my_fraction))
#print(my_fraction)
print(' ')

# Test fraction addition
print('Add fractions:')
print('your_fraction = Fraction(6, 7)')
print('sum_fraction = my_fraction + your_fraction')
your_fraction = Fraction(6, 7)
sum_fraction = my_fraction + your_fraction

print(sum_fraction)
print(' ')

# Test Greatest Common Denominator
print('Test Greatest Common Denominator')
print('gcd(203, 10) = {}'.format(gcd(203, 10)))


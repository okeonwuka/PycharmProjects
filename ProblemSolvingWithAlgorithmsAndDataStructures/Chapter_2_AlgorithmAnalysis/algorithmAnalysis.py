import time

# 1 algorithm to compute first n integers


def sum_of_n(n):
    the_sum = 0
    for i in range(1, n+1):
        the_sum = the_sum + i
    return the_sum

# Test sum_of_n function
n = 6
print('The sum of first %d Integers is: %d' % (n, sum_of_n(n)))
n = 10
print('The sum of first %d Integers is: %d' % (n, sum_of_n(n)))
n = 1000000
print('The sum of first %d Integers is: %d' % (n, sum_of_n(n)))
# ====================================================================================


# 2 Modify sum_of_n(n) to incorporate time, making it sum_of_n_2(n)

def sum_of_n_2(n):
    the_sum = 0
    start = time.time()
    for i in range(1, n+1):
        the_sum = the_sum + i
    end = time.time()
    return the_sum, end - start

# Test sum_of_n_2 function
n = 6
print('The sum of first 6 Integers is: %d and it took %10.7f seconds to run' % (sum_of_n_2(n)))
# n = 10
# print('The sum of first %d Integers is: %d and it took %1.17f seconds to run' % (n, sum_of_n_2(n)))
# n = 1000000
# print('The sum of first %d Integers is: %d and it took %10.7f seconds to run' % (n, sum_of_n_2(n)))


# consecutive iterations for sum of first 100,000,000 integers:
for i in range(14):
    print('Sum is %d and it required %10.7f seconds' % sum_of_n_2(i))


# ====================================================================================


# 3 Modify sum_of_n_(n)_2 to another algorithm, making it sum_of_n_3(n)

def sum_of_n_3(n):
    start = time.time()
    the_sum = (n * (n + 1)) / 2
    end = time.time()
    return the_sum, end - start

# consecutive iterations for sum of first 100,000,000 integers with this algorithm:
for i in range(14):
    print('Sum is %d and it required %10.7f seconds' % sum_of_n_3(i))


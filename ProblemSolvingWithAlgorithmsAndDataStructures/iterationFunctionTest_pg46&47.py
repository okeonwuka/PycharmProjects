# Nested Iteration test
# create a function that does nested iteration

def iteration_function(n):
    for i in range(n + 1):
        for j in range(n + 1):
            x = i * i
            y = j * j
            z = i * j
            print("when i=%1d and j=%1d... x = %1d, y = %1d, z = %1d " % (i, j, x, y, z))
    print(" when n = %1d, after 2 iterations the value of  x = %1d, the value of y = %1d, the value of z = %1d " % (
    n, x, y, z))


iteration_function(100)

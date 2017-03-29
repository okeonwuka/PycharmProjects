# =================================================
#  Interface to collect user input
# =================================================
# Initialize with empty list
datalist = []

# Initialize escape parameter to end population of datalist
datapoint = ' '

# Start a loop that will run until user enters 'quit'
while datapoint != 'quit':
    # Input data point.
    datapoint = input('Please enter  the numbers that you want to calculate the outlier on. Enter quit once done : ')
    if datapoint != 'quit':
        datapoint = int(datapoint)
        datalist.append(datapoint)

# Print out entire list
print(datalist)


# =================================================
#  Calculate Median
# =================================================
#  Arrange elements numerically
datalist.sort()
print(datalist)

# Get total of elements in datalist
totElementsInList = len(datalist)
print("the number of elements in datalist ie the 'rank' is : {}".format(totElementsInList))

# Calculate median
if totElementsInList%2 == 1:
    print("The data set has an odd number of elements, therefore the rank is odd")
    print("Median Formula for odd rank is '((No of positions/elements in data set)+1 )/2'")
    medianPositionForOddRank1 = ((totElementsInList + 1)/2) -1  #NOTE:  We need to subtract an extra 1 to account for the fact indices for list start counting from 0
    print("The median is the element in the {}th position, but after offsetting the count by 1 to compensate for the fact indices for lists start counting from 0, the median is in the {}th position".format(medianPositionForOddRank1+1, medianPositionForOddRank1))
    # convert medianPositionForOddRank1 from float to int so we can use 'pop' method for a list
    medianPositionForOddRank2 = int(medianPositionForOddRank1)
    print("The median is {}".format(datalist[medianPositionForOddRank2]))
else:
    print("The data set has an even number of elements, therefore the rank is even")
    print("Median Formula for even rank is '[(No of positions/elements in data set)/2 + ((No of positions/elements in data set)+1)/2]/2  '")
    medianPositionForEvenRank = (totElementsInList/2 + (totElementsInList/2)+1)/2
    print("the median is the element in the {}th position".format(medianPositionForEvenRank))
    # To get the actual element that is in the 'medianPositionForEvenRank' th position,
    # 1. subtract 1 from  medianPositionForEvenRank  to account for the fact indices for list start counting from 0.
    # 2. add subtract 0.5 and add 0.5 to the result of (medianPositionForEvenRank-1), to get the indices of the 2 elements in the list that bound the medianPositionForEvenRank' th position
    # 3. Add these 2 elements and then divide them by 2 to get the actual median element

    # Get index of element in lower bound of (medianPositionForEvenRank-1)
    lowerBoundIndex = (medianPositionForEvenRank-1) - 0.5
    # convert to lowerBoundIndex to an int from float
    intLowerBoundIndex = int(lowerBoundIndex)
    # Extract actual element in the lower bound
    lowerBoundElement = datalist[intLowerBoundIndex]

    # Get index of element in upper bound of (medianPositionForEvenRank-1)
    upperBoundIndex = (medianPositionForEvenRank-1) + 0.5
    # convert to upperBoundIndex to an int from float
    intUpperBoundIndex = int(upperBoundIndex)
    # Extract actual element in the upper bound
    upperBoundElement = datalist[intUpperBoundIndex]

    # Get actual median for Even rank
    medianForEvenRank = (lowerBoundElement + upperBoundElement)/2
    print("The median is {}".format(medianForEvenRank))

# # Input sample List
# sampleList = [81,500,89,25,67,24,56,90,23,54,222,66,77,88,433,556745,3475368,24523,]
#
#
# # Create function to Look for minimum number in sampleList
# # for i in range(len(sampleList)):
# #     if sampleList[i] > sampleList[i+1]:
# #         sampleList.pop(i)
# # print(sampleList)
#
# for i in sampleList:
#     if i > y:
#         sampleList.pop(x)
# print(sampleList)
#

# The Code below gave me and infinite loop
sampleList = [8, 5, 1, 7]

pos0 = 0
pos1 = 1

while pos1 <= len(sampleList):
    if sampleList[pos0] < sampleList[pos1]:
        sampleList.pop(pos0)
        pos0 = + 1
        pos1 = + 1
print(sampleList)

# Correction attempt_1
sampleList = [8, 5, 1, 7]

pos0 = 0
# pos1 =1
still_ok = True

while pos0 <= len(sampleList) and still_ok:
    pos1 = 1
    found = False
    while pos1 < len(sampleList) and not found:
        if sampleList[pos0] < sampleList[pos1]:
            sampleList.pop(pos1)
            found = True
            pos0 = + 1
            pos1 = + 1
print(sampleList)

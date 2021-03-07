# O(n) time // O(1) since all operations include swapping or inplace
def findThreeLargestNumbers(array):
    largestThree = [None, None, None]
    for i in array:
        compareAndUpdate(largestThree, i)
    return largestThree

def compareAndUpdate(threeLargest, num):
    if threeLargest[2] is None or num > threeLargest[2]:
        threeLargest = swap(threeLargest, 2, num)
    elif threeLargest[1] is None or num > threeLargest[1]:
        threeLargest = swap(threeLargest, 1, num)
    elif threeLargest[0] is None or num > threeLargest[0]:
        threeLargest = swap(threeLargest, 0, num)
    return threeLargest

def swap(threeLargest, idx, num):
    if idx == 0:
        threeLargest[0] = num
    elif idx == 1:
        threeLargest[0] = threeLargest[1]
        threeLargest[1] = num
    elif idx == 2:
        threeLargest[0] = threeLargest[1]
        threeLargest[1] = threeLargest[2]
        threeLargest[2] = num
    return threeLargest

findThreeLargestNumbers([55, 7, 8, 3, 43, 11])

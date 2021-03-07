def smallestDifference(arrayOne, arrayTwo):
    i = 0
    j = 0
    arrayOne.sort()
    arrayTwo.sort()
    smallest = float("inf")
    small_set = []

    while i < len(arrayOne) and j < len(arrayTwo):
        first = arrayOne[i]
        second = arrayTwo[j]
        current = abs(second - first)

        if first < second:
            i += 1

        elif second < first:
            j += 1

        else:
            return [first, second]

        if smallest > current:
            smallest = current
            small_set = [first, second]

    return small_set

smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17])
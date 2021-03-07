def getNthFib(n):
    i = 0
    j = 1
    curFib = 1
    while curFib < n-2:
        swap = i
        i = j
        j = swap + i
        curFib += 1
    return j



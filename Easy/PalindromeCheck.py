def isPalindrome(string):
    rightIdx = 0
    leftIdx = len(string) - 1
    while rightIdx < leftIdx:
        if string[rightIdx] != string[leftIdx]:
            return False
        rightIdx += 1
        leftIdx -= 1
    return True


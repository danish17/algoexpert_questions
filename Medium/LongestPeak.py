def longestPeak(array):
    largestPeak = 0
    idx = 1
    while idx < len(array) - 1:
        isPeak = array[idx - 1] < array[idx] > array[idx + 1]
        if not isPeak:
            idx += 1
            continue

        leftIdx = idx - 2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx -= 1

        rightIdx = idx + 2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1

        peakLength = rightIdx - leftIdx - 1

        largestPeak = max(largestPeak, peakLength)
        idx = rightIdx
    return largestPeak
def groupAnagrams(words):
    grouped = {}
    for word in words:
        sortedWord = ''.join(sorted(word))
        if sortedWord in grouped:
            grouped[sortedWord].append(word)
        else:
            grouped[sortedWord] = [word]

    return list(grouped.values())

groupAnagrams(['xii', 'xii', 'ixi', 'ch', 'hc'])
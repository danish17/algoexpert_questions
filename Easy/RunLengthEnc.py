#O(n) | O(n)
def runLengthEncoding(string):
    idx = 0
    length = 1
    enc = []
    for idx in range(1, len(string)):
        if string[idx] == string[idx-1] and length <= 8:
            length += 1
        elif string[idx] != string[idx - 1]:
            enc = addToEnc(string[idx - 1], length, enc)
            length = 1
        elif string[idx] == string[idx-1] and length > 8:
            enc = addToEnc(string[idx - 1], length, enc)
            length = 1
    enc.extend([str(length), string[len(string)-1]])
    return "".join(enc)

def addToEnc(char, length, enc):
    enc.extend([str(length), char])
    return enc

runLengthEncoding("AAAAAAAAAAAAABBCCCCDD")
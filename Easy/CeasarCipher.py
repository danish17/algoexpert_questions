def caesarCipherEncryptor(string, key):
    # Write your code here.
    string = string.lower()
    encrypted = ""
    for x in string:
        if ord(x) + key % 26 > ord('z'):
            encrypted += chr(ord('a') + (key % 26) - (ord('z') - ord(x)) - 1)
        else:
            encrypted += chr(ord(x) + (key % 26))
    return encrypted

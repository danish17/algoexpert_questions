# Convert integer to Roman numerals
# I = 1
# IV = 4
# V = 5
# IX = 9
# X = 10
# XI = 11
# L = 50
# C = 100
# D = 500
# M = 1000
def breakUp(val):
    digits = [int(x) for x in list(str(val))]
    multiplier = 1
    for idx in reversed(range(0, len(str(val)))):
        digits[idx] = digits[idx]*multiplier
        multiplier *= 10
    return digits

def makeFromBasic(val, dict):
    roman = []
    if 1 < int(val) < 4:
        roman = [dict['1'] * int(val)]
        return roman
    elif 5 < int(val) < 9:
        roman.append(dict['5'])
        roman.extend([dict['1'] * (int(val) - 5)])
        return roman
    elif 10 < int(val) < 50:
        if int(val) == 40:
            return ['XL']
        roman.extend([dict['10'] * (int(val) // 10)])
        return roman
    elif 50 < int(val) < 100:
        roman.append(dict['50'])
        roman.extend(makeFromBasic(int(val) - 50, dict))
        return roman
    elif 100 < int(val) < 500:
        roman.extend([dict['100'] * (int(val) // 100)])
        return roman
    elif 500 < int(val) < 1000:
        roman.append(dict['500'])
        roman.extend(makeFromBasic(int(val) - 500, dict))
        return roman
def convertIntToRoman(val):
    predefined = {
        '1': 'I',
        '4': 'IV',
        '5': 'V',
        '9': 'IX',
        '10': 'X',
        '11': 'XI',
        '40': 'XL',
        '50': 'L',
        '90': 'XC',
        '100': 'C',
        '400': 'CD',
        '500': 'D',
        '900': 'CM',
        '1000': 'M', }

    roman = []
    if str(val) in predefined.keys():
        return predefined[str(val)]
    else:
        digits = breakUp(int(val))
        for x in digits:
            if str(x) in predefined:
                roman.append(predefined[str(x)])
            else:
                roman.extend(makeFromBasic(val, dict))
        return roman

convertIntToRoman(12)
x.extend([{'a':'10'}['a'] * 3])
def balancedBrackets(string):
    openBrack = "{[("
    closeBrack = "])}"
    opposites = {
        '}': '{',
        ')': '(',
        ']': '[',
    }
    stack = []
    for s in string:
        if s in openBrack:
            stack.append(s)
        elif s in closeBrack:
            if len(stack) == 0:
                return False
            if stack[-1] == opposites[s]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

if __name__ == '__main__':
    string = input()
    balancedBrackets(string)
# def balancedBrackets(string):
#     openCount = {}
#     openPars = ['(', '{', '[']
#     closePars = [')', '}', ']']
#     for par in string:
#         if par in openPars:
#             if par not in openCount.keys():
#                 openCount[par] = 1
#             else:
#                 openCount[par] += 1
#         elif par in closePars:
#             if getOpposite(par) not in openCount.keys():
#                 return False
#             else:
#                 openCount[getOpposite(par)] -= 1
#         else:
#             continue
#     if any(openCount.values()) != 0:
#         return False
#     else:
#         return True
#
# def getOpposite(par):
#     pars = {
#         '}': '{',
#         ']': '[',
#         ')': '(',
#     }
#     return pars.get(par)
#
# balancedBrackets('{[[[[({(}))]]]]}')


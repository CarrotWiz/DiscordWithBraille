# toBraille.py functions to convert a string to a braille matrix to a binary string representation with 32 4x2 braille characters

import re

# each letter's braille matrix representation
letterConstants = {
    'a': [[1,0],[0,0],[0,0],[0,0]], # lowercase letters a-z
    'b': [[1,0],[1,0],[0,0],[0,0]],
    'c': [[1,1],[0,0],[0,0],[0,0]],
    'd': [[1,1],[0,1],[0,0],[0,0]],
    'e': [[1,0],[0,1],[0,0],[0,0]],
    'f': [[1,1],[1,0],[0,0],[0,0]],
    'g': [[1,1],[1,1],[0,0],[0,0]],
    'h': [[1,0],[1,1],[0,0],[0,0]],
    'i': [[0,1],[1,0],[0,0],[0,0]],
    'j': [[0,1],[1,1],[0,0],[0,0]],
    'k': [[1,0],[0,0],[1,0],[0,0]],
    'l': [[1,0],[1,0],[1,0],[0,0]],
    'm': [[1,1],[0,0],[1,0],[0,0]],
    'n': [[1,1],[0,1],[1,0],[0,0]],
    'o': [[1,0],[0,1],[1,0],[0,0]],
    'p': [[1,1],[1,0],[1,0],[0,0]],
    'q': [[1,1],[1,1],[1,0],[0,0]],
    'r': [[1,0],[1,1],[1,0],[0,0]],
    's': [[0,1],[1,0],[1,0],[0,0]],
    't': [[0,1],[1,1],[1,0],[0,0]],
    'u': [[1,0],[0,0],[1,1],[0,0]],
    'v': [[1,0],[1,0],[1,1],[0,0]],
    'w': [[0,1],[1,1],[0,1],[0,0]],
    'x': [[1,1],[0,0],[1,1],[0,0]],
    'y': [[1,1],[0,1],[1,1],[0,0]],
    'z': [[1,0],[0,1],[1,1],[0,0]],
    'U': [[0,0],[0,0],[0,1],[0,0]], # uppercase letter constant
    'N': [[0,1],[0,1],[1,1],[0,0]], # number constant
}

# each number's braille matrix equivalence
numberConstants = {
    '1' : 'a',
    '2' : 'b',
    '3' : 'c',
    '4' : 'd',
    '5' : 'e',
    '6' : 'f',
    '7' : 'g',
    '8' : 'h',
    '9' : 'i',
    '0' : 'j',
}

# converts a lowercase/numberless OR uppercase/number constant character to braille matrix
def letterToMatrix(ch, braille, pos):
    brailleLetter = letterConstants.get(ch)
    braille[pos] = brailleLetter

# converts a lowercase/numberless OR uppercase/number constant string to braille matrix list
def lowerCaseStringToMatrix(str, braille):
    letters = list(str)
    pos = 0
    for letter in letters:
        letterToMatrix(letter, braille, pos)
        pos += 1
        if pos >= 32:
            break

# replaces all uppercase letters in a string with uppercase constant and lowercase letter equivalence
def replaceUppercase(str):
    newStr = ""
    res = re.split('(?=[A-Z])', str)
    for snip in res:
        if len(snip) > 0 and snip[0].isupper():
            snip = "U" + snip[0].lower() + snip[1:]
        newStr += snip
    if len(res) == 0:
        return str
    return newStr

# replaces all numbers in a string with number constant and letter equivalence
def replaceNumbers(str):
    newStr = ""
    res = re.findall('(\d+|[A-Za-z]+)', str)
    for snip in res:
        if snip.isnumeric():
            newSnip = "N"
            for ch in snip:
                newSnip += numberConstants.get(ch)
            snip = newSnip
        newStr += snip
    return newStr

# removes all whitespace in a string
def removeWhitespace(str):
    return ''.join(str.split())

# converts braille matrix list to binary representation of the matrix for a 32x8 grid
def brailleToBinary(braille):
    binaryList = [0] * 256
    topLeft = 0
    for b42 in braille:
        binaryList[topLeft] = b42[0][0]
        binaryList[topLeft+1] = b42[0][1]
        binaryList[topLeft+32] = b42[1][0]
        binaryList[topLeft+33] = b42[1][1]
        binaryList[topLeft+64] = b42[2][0]
        binaryList[topLeft+65] = b42[2][1]
        binaryList[topLeft+96] = b42[3][0]
        binaryList[topLeft+97] = b42[3][1]
        topLeft += 2
        if topLeft%32 == 0:
            topLeft += 96
    return binaryList

# returns string representation of the binary list
# needs to be a string in order to not get rid of leading zeros
def printBinary(binaryList):
    s = ''.join(str(n) for n in binaryList)
    # for x in range(8):                        # uncomment these two lines to print the braille's 32x8 grid
    #     print(s[x * 32: x*32 + 31])

    # print(s) # uncomment this line to see the 256 char binary string representation of the braille matrix
    return s

# converts a string to a binary representation of a 32x8 braille grid
def stringToBinary(str):
    braille = [[[0]*2]*4]*32
    str = removeWhitespace(str)
    str = replaceUppercase(str)
    str = replaceNumbers(str)
    lowerCaseStringToMatrix(str, braille)
    binaryList = brailleToBinary(braille)
    return(printBinary(binaryList))
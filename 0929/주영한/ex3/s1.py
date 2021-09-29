table = {
    '0' : 0,
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    'A' : 10,
    'B' : 11,
    'C' : 12,
    'D' : 13,
    'E' : 14,
    'F' : 15,
}

codes = {
    "001101" : 0,
    "010011" : 1,
    "111011" : 2,
    "110001" : 3,
    "100011" : 4,
    "110111" : 5,
    "001011" : 6,
    "111101" : 7,
    "011001" : 8,
    "101111" : 9
}

def to_binary(char):
    result = ""
    decimalNum = table[char]
    while decimalNum:
        result = str(decimalNum % 2) + result
        decimalNum = decimalNum // 2
    if len(result) != 4:
        result = "0" * (4 - len(result)) + result
    return result

def decode(binaryMessage):
    result = []
    end_idx = len(binaryMessage) - 1
    while end_idx >= 6:
        if binaryMessage[end_idx] == '1' and codes.get(binaryMessage[end_idx - 5 : end_idx + 1]) != None:
            result = [codes[binaryMessage[end_idx - 5 : end_idx + 1]]] + result
            end_idx -= 6
            continue
        end_idx -= 1
    return result

binaryNumber = ""
messages = "0DEC"
# messages = "0269FAC9A0"
result = ""
for message in messages:
    result += to_binary(message)

print(*decode(result))
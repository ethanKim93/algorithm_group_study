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

def to_binary(char):
    result = ""
    decimalNum = table[char]
    while decimalNum:
        result = str(decimalNum % 2) + result
        decimalNum = decimalNum // 2
    if len(result) != 4:
        result = "0" * (4 - len(result)) + result
    return result

def to_decimal(message):
    temp = 0
    for idx in range(len(message)):
        if message[len(message) - 1 - idx] == '1':
            temp += 2 ** idx
    return temp

def divide(binaryMessage):
    end_idx = 7
    while end_idx < len(binaryMessage):
        print(to_decimal(binaryMessage[end_idx - 7 : end_idx]), end=" ")
        end_idx += 7
    print(to_decimal(binaryMessage[end_idx - 7 : len(binaryMessage)]))

binaryNumber = ""
messages = "0F97A3"
# messages = "01D06079861D79F99F"
result = ""
for message in messages:
    result += to_binary(message)
divide(result)
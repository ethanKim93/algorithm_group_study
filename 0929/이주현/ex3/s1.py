input_data = list(map(str, input()))
# 0DEC

num16 = {
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

binary = ''
for i in range(len(input_data)):
    num10 = num16[input_data[i]]
    tmp = []
    while num10 > 1:
        tmp.append(str(num10 % 2))
        num10 //= 2
    tmp.append(str(num10))
    tmp = tmp[::-1]
    while len(tmp) < 4:
        tmp = ['0'] + tmp
    binary += "".join(tmp)

patterns = {
    '001101': 0,
    '010011': 1,
    '111011': 2,
    '110001': 3,
    '100011': 4,
    '110111': 5,
    '001011': 6,
    '111101': 7,
    '011001': 8,
    '101111': 9
}
data = []
start = 0
for pattern in patterns:
    for i in range(start, len(binary) - len(pattern)):
        if binary[i:i+len(pattern)] == pattern:
            data.append(patterns[pattern])
            start = i + len(pattern)
            break
print(data)



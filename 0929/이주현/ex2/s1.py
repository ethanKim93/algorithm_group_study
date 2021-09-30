input_data = list(map(str, input()))
# 0F97A3

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

data = []

for i in range(0, len(binary), 7):
    if len(binary) - i >= 7:
        tmp = binary[i:i+7]
    else:
        tmp = binary[i:]
    result = 0
    for j in range(len(tmp)):
        result += int(tmp[j]) * (2**(len(tmp) - j - 1))
    data.append(result)

print(data)

input_data = input()

data = []

for i in range(0, len(input_data), 7):
    if len(input_data) - i >= 7:
        tmp = input_data[i:i+7]
    else:
        tmp = input_data[i:]
    result = 0
    for j in range(len(tmp)):
        result += int(tmp[j]) * (2**(len(tmp) - j - 1))
    data.append(result)

print(data)


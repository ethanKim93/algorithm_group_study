N = '0000000111100000011000000111100110000110000111100111100111111001100111'
arr = []
for i in range(0, len(N), 7):
    arr.append(N[i:i+7])
print(arr)

for i in range(len(arr)):
    result = 0
    for j in range(6, -1, -1):
        if arr[i][j] == '1':
            result += 2**(6-j)
    print(result)
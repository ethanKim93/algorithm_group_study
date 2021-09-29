a = '01D06079861D79F99F'

cnt = 0
result = ''
for i in range(len(a)):
    if cnt == 0:
        cnt += 1
    if cnt < 8:
        result += a[i]
        cnt += 1
    if cnt == 8:
        print(int("0x" + result, 16), end=', ')
        result = ''
        cnt = 0

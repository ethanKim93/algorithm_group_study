arr ='0000000111100000011000000111100110000110000111100111100111111001100111'

bi = [64, 32, 16, 8, 4, 2, 1]
a = []
c = 0
num = []

for i in range(len(arr)):
    b = int(arr[i])
    i = (i % 7)
    a.append(b*bi[i])

for j in range(len(arr)):
    c += a[j]
    j = (j % 7)
    if j == 6:
        num.append(c)
        c = 0

print(num)









import sys
#2진수->10진수
sys.stdin = open('input.txt')
binaryarr = input()
k = 7
for i in range(0, len(binaryarr), k):
    result = int(binaryarr[i:k + i], 2)
    print(result, end=' ')

print()
for i in range(0, len(binaryarr), k):
    num = binaryarr[i:k + i]
    cac = 0
    for j in range(k):
        if num[j] == "1":
            cac += 2 ** ((k-1)-j)
    print(cac, end=' ')

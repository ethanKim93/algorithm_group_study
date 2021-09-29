# import sys
# sys.stdin = open('input.txt')

n = list('0F97A3')
arr = ''

for i in range(len(n)):
    word = '0x' + n[i]
    for j in range(3,-1,-1):
        arr += "1" if (1<<j) & int(word, 16) else "0"
print(arr)
arr = list(map(int,arr))



i = 0
while i != len(arr):
    sum = 0
    for a in range(7):
        sum += arr[i]*(2**(6-a))
        i += 1
    print(sum)





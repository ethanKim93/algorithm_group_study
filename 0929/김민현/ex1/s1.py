import sys
sys.stdin = open('input.txt')

data = input()
for i in range(len(data)//7):
    binary = data[:7]
    ans = 0
    for j in range(len(binary)):
        if binary[6-j] == '1':
            ans += 2**j
    print(ans)
    data = data[7:]
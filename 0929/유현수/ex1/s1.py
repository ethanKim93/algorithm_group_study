import sys
sys.stdin = open('input.txt')

n = input()
for i in range(10):
    tmp = n[i:i+7][::-1]
    print(tmp)
    output = 0
    for j in range(7):
        if int(tmp[j]):
            output += 1 << j
    print(output)

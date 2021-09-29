import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    data = input()
    bit = ''
    for i in data:
        for j in range(3,-1,-1):
            bit += "1" if int(i,16) & (1<<j) else "0"

    while len(bit) > 7:
        print(int(bit[:7],2),end=',')
        bit = bit[7:]
    print(int(bit,2))

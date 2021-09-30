import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N,hexNums = input().split()
    ans = ''
    #47FE
    for hexNum in hexNums:
        for i in range(3,-1,-1):
            ans += '1' if int(hexNum,16) & (1<<i) else "0"
    print('#{} {}'.format(tc,ans))

    # 0100 #4
    # 1000 #(1<<3)
    # 0100 #(1<<2)
    # 0010 #(1<<1)
    # 0001 #(1<<0)
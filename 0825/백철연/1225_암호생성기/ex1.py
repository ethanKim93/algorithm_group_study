import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    Q = list(map(int, input().split()))

    i = 1
    temp = []

    while 1:
        if i > 5:
            i = 1
        temp = Q.pop(0) - i
        if temp <= 0:
            Q.append(0)
            break
        Q.append(temp)
        i += 1

    result = ' '.join(str(s) for s in Q)
    print('#{} {}'.format(tc,result))
import sys
sys.stdin = open("s_input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    result = []
    stop = [0 for _ in range(5001)]
    for _ in range(N):
        a, b = map(int,input().split())
        for i in range(a, b+1):
            stop[i] += 1
    P = int(input())
    for _ in range(P):
        result.append(stop[int(input())])
    print('#{} {}'.format(tc, ' '.join(map(str,result))))

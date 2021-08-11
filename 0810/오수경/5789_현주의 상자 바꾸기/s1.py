import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    list_a = [0]*N

    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for a in range(L-1, R):
            list_a[a] = i


    box = ' '.join(map(str, list_a))
    print('#{} {}'.format(tc, box))


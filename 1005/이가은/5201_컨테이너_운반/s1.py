import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())

    container = sorted(list(map(int,input().split())),reverse=True)
    truck = sorted(list(map(int,input().split())), reverse=True)

    result = [0]*M

    for n in range(N):
        for m in range(M):
            if truck[m] >= container[n]:
                if not result[m]:
                    result[m] += container[n]
                    break

    ans = sum(result)
    print('#{} {}'.format(tc, ans))
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, (input().split())))

    for i in range(0, N-1):
        min_idx = i
        for j in range(i+1, N):
            if ai[min_idx] > ai[j]:
                min_idx = j
        ai[i], ai[min_idx] = ai[min_idx], ai[i]

    newone = []
    for i in range(1, 6):
        newone.append(ai[-i])
        newone.append(ai[i-1])

    print('#{}'.format(tc), end=' ')
    print(*newone)
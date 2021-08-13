import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))
    result = []

    # 선택정렬 5개
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if ai[minIdx] > ai[j]:
                minIdx = j
        ai[minIdx], ai[i] = ai[i], ai[minIdx]

    for i in range(5):
        result.append(ai[N -1 -i])
        result.append(ai[i])

    print('#{}'.format(tc), end=' ')
    print(*result)
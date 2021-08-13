import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    s = list(map(int, input().split()))

    for i in range(N-1, 0, -1): # 버블소트
        for j in range(0, i):
            if s[j] > s[j+1]:
                s[j], s[j+1] = s[j+1], s[j]

    spe_sort = [0 for _ in range(10)]
    i = 0
    j = 0
    while True:
        spe_sort[i] = s[N-1-j]
        spe_sort[i+1] = s[j]
        j += 1
        i += 2
        if i == 10:
            break
    print('#{}'.format(tc), end=" ")
    print(*spe_sort)

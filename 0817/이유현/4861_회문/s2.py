import sys
sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    ans = ''

    for i in range(N-M+1):
        for j in range(N):
            pal = []
            for p in [row[j] for row in arr[i:i+M]]:
                pal += p
            
            if pal == pal[::-1]:
                ans = pal
            break
        break
    print('#{}'.format(tc), end=' ')
    for p in ans:
        print(p, end='')
    print()




import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    ans = []

    for i in range(N):
        for j in range(N-M+1):
            pal = arr[i][j:j+M]
            if pal == pal[::-1]:
                print('#{}'.format(tc), end=' ')
                for p in pal:
                    print(p, end='')
                print()
        
    else:
        for i in range(N-M+1):
            for j in range(N):
                pal = []
                for p in [row[j] for row in arr[i:i+M]]:
                    pal += p
                
                if pal == pal[::-1]:
                    print('#{}'.format(tc), end=' ')
                    for p in pal:
                        print(p, end='')
                    print()




        


import sys
sys.stdin = open('input.txt')

T = int(input())

def tower(idx, tot):
    global minimum

    if tot >= B:
        if minimum > tot - B:
            minimum = tot - B
        return

    if idx == N:
        return
    
    tower(idx+1, tot+S[idx])
    tower(idx+1, tot)


for tc in range(1, T+1):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))
    minimum = 987654321
    tower(0, 0)
    print('#{} {}'.format(tc, minimum))
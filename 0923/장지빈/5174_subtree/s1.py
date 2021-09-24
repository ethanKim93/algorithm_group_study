import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def order(i):
    global cnt
    if not i:
        return
    cnt += 1
    order(L[i])
    order(R[i])

for tc in range(1, int(input())+1):
    E, N = map(int, input().split())
    NE = list(map(int, input().split()))
    L = [0] * (E+2)
    R = [0] * (E+2)
    cnt = 0
    # print(NE)
    for i in range(0, len(NE), 2):
        if L[NE[i]]:
            R[NE[i]] = NE[i+1]
        else:
            L[NE[i]] = NE[i+1]

    order(N)

    print(f'#{tc} {cnt}')
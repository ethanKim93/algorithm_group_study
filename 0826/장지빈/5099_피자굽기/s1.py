import sys
sys. stdin = open('input.txt')

def pizza():
    pit = []
    for _ in range(N):
        pit.append(pizidx.pop(0))
    while len(pit) > 1:
        piz = pit.pop(0)
        piz[1] //= 2
        if piz[1]:
            pit.append(piz)
        else:
            if len(pizidx):
                pit.append(pizidx.pop(0))
    return pit

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    Ci = input().split()
    pizidx = [[i+1, int(Ci[i])] for i in range(M)]
    print('#{} {}'.format(tc, pizza()[0][0]))
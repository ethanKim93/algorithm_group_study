import sys
sys.stdin = open("input.txt")
#5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 컨테이너수 N, 트럭 수 M
    w = sorted(list(map(int, input().split())),reverse=True) # 화물의 무게
    t = sorted(list(map(int, input().split())),reverse=True) # 적재 용량

    res = 0
    for i in range(M):
        for j in range(len(w)):
            if t[i] >= w[j]:
                res += w[j]
                w.remove(w[j])
                break
    print('#{} {}'.format(tc, res))
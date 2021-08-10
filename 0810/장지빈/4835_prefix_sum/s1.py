import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    ai = list(input().split())
    dif = []
# 각 변수를 입력받고, dif라는 list 변수 설정

    for a in range(N-M+1):
        ls = 0
        for x in range(a, a+M):
            ls += int(ai[x])
        dif.append(ls)
# dif list에 각 구간별 합 저장

    difMax = dif[0]
    difMin = dif[0]

    for y in dif:
        if y > difMax:
            difMax = y
        if y < difMin:
            difMin = y
# 대소 비교 후 max - min 결과값 저장 및 출력
    result = difMax - difMin
    print('#{} {}'.format(i+1, result))
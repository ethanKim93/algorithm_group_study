import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    wt = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    ans = 0
    for i in range(M):
        tem = []
        for j in range(N):
            if truck[i] >= wt[j]: # 무게가 트럭 용량보다 작거나 같으면
                tem.append(wt[j]) # 적재
        if tem:                   # tem에 값이 있으면
            ans += max(tem)       # 최댓값을 ans에 더해줌
            for j in range(N):
                if wt[j] == max(tem):
                    wt[j] = 0           # 적재했던 컨테이너는 다시 안봐도 되기 때문에 0으로
                    break
    print("#{} {}".format(tc, ans))


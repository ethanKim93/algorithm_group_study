import sys
sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1, T+1):
    # N : 컨테이너 수, M: 트럭 수
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    ans = 0 
    # 컨테이너 무게와, 트럭 한계 무게 오름차순 정렬
    containers.sort()
    trucks.sort()
    i, j = M-1,  N-1
    while i>=0 and j>=0:
        # 한계 무게가 큰 트럭부터 컨테이너 무게가 무거운거부터 실을 수 있으면
        if trucks[i] >= containers[j]:
            ans += containers[j]
            # 다음 트럭으로
            i -= 1
        # 다음 컨테이너로
        j -= 1

    print('#{} {}'.format(tc, ans))

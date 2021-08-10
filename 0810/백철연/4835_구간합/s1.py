import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    sums = []
    for i in range(N - M + 1):        # M만큼 더해나갈 구간 설정?
        result = 0
        for j in range(i, i + M):     # j를 1씩 증가시키며, 주어진 구간만 큼 result에 더 해줌
            result += nums[j]
        sums.append(result)           # 3개씩 더해진 값을 빈 리스트에 할당

    for i in range(0, len(sums)-1):
        for j in range(i + 1, len(sums)):
            if sums[j] < sums[i]:
                sums[j], sums[i] = sums[i], sums[j]
    #선택정렬
    print('#{} {}'.format(tc,sums[-1]-sums[0])) #최댓값 - 최솟값







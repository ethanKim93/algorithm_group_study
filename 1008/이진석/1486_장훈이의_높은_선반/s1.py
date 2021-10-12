import sys
sys.stdin = open('input.txt')
def sum_height(idx, height, visit):
    global result
    if height >= result:            # 현재 찾은 높이 보다 클경우 종료
        return
    if B <= height < result:        # 현재 높이보다 낮으면서 선반보다 크거나 같을경우 result 갱신
        result = height
        return
    if idx == N:
        return

    for i in range(idx, len(people)):   #
        if visit & (1 << i):            # i번째 점원이 탑에 참여하지 않았을 때 (i번째 비트가 1일때)
            visit &= ~(1 << i)          # i번째 점원 탑에 참여 (i번째 비트 0으로 갱신) : 1을 왼쪽으로 i번 shift(i번째 비트만 1) > 비트 반전 > &(AND)연산
            sum_height(i, height+people[i], visit)  # 다음 점원 체크
            visit |= (1 << i)           # 탑에서 제외 (i번째 비트 1로 갱신) : 1을 왼쪽으로 i번 shift(i번째 비트만 1) > |(OR)연산

for tc in range(1, int(input())+1):
    N, B = map(int, input().split())            # N : 점원의 수, B : 선반의 높이
    people = list(map(int, input().split()))    # 점원들의 키
    result = 10000*N                            # 선반보다 크거나 같은 탑중에 가장 작은 탑
    visited = (1 << N)-1                        # 점원의 탑 참여 여부 (default : 1)
    sum_height(0, 0, visited)
    answer = result-B
    print('#{} {}'.format(tc, answer))    # 탑과 선반과의 차이 출력

import sys
sys.stdin = open('sample_input.txt', 'r')


# x,y 인덱스가 하나도 겹치지 않게 골고루 들어가라는 조건이었다.
# 이를 위해 y를 idx 로 정하고
# x는 반복문을 통해서 해결했다.


# 비용 계산 함수
# 인덱스와 합을 받을 예정
# idx 값은 y값 이라고 생각하면 된다.
def lowest_price(idx, total):
    global result

    if total >= result:
        # 시간초과와 계산 번거로움줄이기 위한 코드
        # 만약 값이 이미 구한 값 초과한다면 종료
        return

    if idx == N:
        # 만약 다 검사를 마쳤다면
        # total 값은 결과값 ( 위에서 이미 걸렀기 때문 )
        result = total
        return

    for i in range(N):
        # N만큼 돌면서 x축 검사
        if not visited[i]:
            # 만약 x의 인덱스가 방문한 적이 없다면
            visited[i] = 1
            # 방문 후 다음 idx 값 살펴보고 다시 돌아오는 과정
            lowest_price(idx + 1, total + V[idx][i])
            visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # N은 제품 수
    V = [list(map(int, input().split())) for _ in range(N)]
    # V는 공장별 생산비용

    visited = [0] * N
    # 방문 체크를 위한 변수
    result = 100 * N
    # 값 비교를 위한 임의의 큰 result 값

    lowest_price(0, 0)

    print('#{} {}'.format(tc, result))

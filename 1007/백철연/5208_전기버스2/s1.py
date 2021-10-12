import sys
sys.stdin = open('sample_input.txt')

# 최종 코드(장지빈)
def check(n, cnt): # n 정류장의 위치 , cnt 충전 횟수
    global ans
    if cnt >= ans:    # 가지치기 , 들고다닌 충전 횟수가 ans보다 크다면 볼 필요가 없으므로 리턴
        return
    if n >= N - 1:
# 최대 정류장 번호에 도착하거나 용량이 커서 넘어가는 경우 들고다닌 충전 횟수와 ans값 비교후 저장
        if ans > cnt:
            ans = cnt
        return
    for i in range(bat[n]):
# bat로 저장한 리스트의 0번째부터 출발, +1을 해주어야 다음 정류장으로 출발 가능
        check(n + i + 1, cnt+1)    # 충전 횟수 +1 /
# 첫 출발인 경우 충전이 아닌 장착이므로 -1 +1로 충전횟수 0회 시작

for tc in range(1, int(input())+1):
    ans = (100**2)+1
    li = list(map(int, input().split()))
    N = li[0]
# 정류장 갯수
    bat = li[1:]
# li에서 정류장의 번호를 제외한 부분만 저장
    charge = 0
    check(0, -1)
# 출발지에서의 배터리 장착은 교환횟수에서 제외한다.

    print('#{} {}'.format(tc, ans))
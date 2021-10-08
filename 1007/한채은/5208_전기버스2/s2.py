# n = 정류장 인덱스
def check(n, cnt):
    global ans
    # 가지치기 (충전한 회수가 더 크면 바로 return)
    if cnt >= ans:
        return
    # n이 N-1보다 크거나 같을 때
    if n >= N - 1:
        # 충전회수가 적어지면 바꾸는 부분
        if ans > cnt:
            ans = cnt
        return

    #
    for i in range(bat[n]):
        # +1 을 넣어줘야 다음으로 넘어갈 수 있음
        # 충전을 해줬으니까 cnt에 +1을 해줌
        check(n + i + 1, cnt+1)

for tc in range(1, int(input())+1):
    ans = (100**2)+1 # 충전값이 최대 10000 + 1
    li = list(map(int, input().split()))
    # 정류장
    N = li[0]
    # 배터리 용량
    bat = li[1:]
    charge = 0
    # 최초로 들어갈때 충전을 한다고 가정하므로 cnt에 -1
    check(0, -1)

    print('#{} {}'.format(tc, ans))
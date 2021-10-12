import sys
sys.stdin = open('sample_input.txt')


# 버스가 가면서 배터리 충전하는 함수
# idx: 정류장의 위치
# cnt: 충전횟수
def bus(idx, cnt):
    global result
    # 더 작은 값이 안나오면 return
    if result < cnt:
        return

    # 만약 목적지를 넘는다면
    if idx >= N:
        result = cnt
        return
    # 한번 충전해서 갈수 있는 곳을 다 둘러보는 반복문
    # 해당 정류장에서 해당하는 배터리로 갈수 있는 경우의 수를 모두 둘러본다.
    for i in range(info[idx], 0, -1):
        bus(idx+i, cnt + 1)


T = int(input())
for tc in range(1, T+1):
    info = list(map(int, input().split()))
    # 0부터 시작하니까 -1 해준다.
    N = info.pop(0) - 1
    # 임의로 result값 설정
    result = 10000
    # 최초 들어갈때 충전을 한다고 가정하므로 cnt에 -1
    bus(0, -1)

    print("#{} {}".format(tc, result))

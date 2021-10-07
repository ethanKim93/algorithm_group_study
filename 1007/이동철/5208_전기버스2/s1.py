import sys
sys.stdin = open('sample_input.txt', 'r')


# 현종일
def charge(now, cnt):          # now : 현재 정류장, cnt : 현재까지 주유횟수
    global result
    battery = charge_area[now] # 현재 배터리를 교체합니다.

    if cnt > result:           # 주유횟수가 최소결과값보다 크다면 가지치기
        return

    if now+battery >= N:       # 현재 정류장 + 현재 배터리가 N보다 크다면
        if cnt <= result:      # 최소결과값 갱신후 리턴
            result = cnt
        return

    for i in range(1, battery+1):
        if now+i < N:
            charge(now+i, cnt+1)


for tc in range(1, int(input())+1):
    charge_area = list(map(int,input().split()))
    N = charge_area[0] # 1번 인덱스부터 쓰기 위해 pop 을 쓰거나 따로 나누지 않음
    result = 100       # 현재 최대값 100 미리 대입

    charge(1, 0)
    print('#{} {}'.format(tc, result))


# # 주영한
# for tc in range(1, int(input()) + 1):
#     charge = list(map(int, input().split()))
#     destination = charge[0] - 1
#     charge = charge[1:]
#     result = -1
#     idx = 0
#     # 가장 멀리 갈 수 있는 경우를 찾아 해당 지역 선택하기
#     while idx < destination:
#         max_pos = idx
#         max_idx = idx
#         for i in range(1, charge[idx] + 1):
#             move = idx + i
#             if move >= destination:
#                 idx = move
#                 break
#
#             if max_pos < move + charge[move]:
#                 max_pos = move + charge[move]
#                 max_idx = i
#         idx += max_idx
#         result += 1
#
#     print("#{} {}".format(tc, result))


# def dfs(idx):
#     global result, charge
#
#     if idx >= len(arr):
#         # 정류장 idx 를 체크하여 종점에 이르기 전까지 충전 횟수를 세준다.
#         # 종점에 이르면 지금까지 충전 횟수 charge 가
#         # 최종 최소 값인 result 보다 작거나 같은지 확인한다.
#         if result >= charge:
#             result = charge
#         return
#
#     if result <= charge:
#         # 재귀호출 과정 중, 유망하지 않으면,
#         # 지금 충전하고 있는 횟수가 이전에 충전이 완료된 횟수를 넘어가면
#         # 굳이 더 따질 필요가 없기 때문에 재귀호출을 return 하여 백트래킹한다.
#         return
#
#     for i in range(idx + arr[idx], idx, -1):
#         # 전기를 충전 하기 위해서는, 예를 들면 1번 정류장이 2칸 움직일 수 있게 충전한다면
#         # 2, 3번 정류장을 갈 수 있다는 뜻이므로
#         # 두개의 정류장을 따져줄 수 있게 반복문(for문)을 돌려 재귀호출 한다.
#         charge += 1
#         dfs(i)
#         # 새로운 정류장에 도달하고자 할때마다 dfs 를 사용하여 재귀호출한다.
#         charge -= 1
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     arr = list(map(int, input().split()))
#
#     station = arr[0]
#     # 그냥 이해를 위해 만든 정류장 개수
#     result = 1000000
#     charge = 0
#     dfs(1)
#
#     print('#{} {}'.format(tc, result - 1))




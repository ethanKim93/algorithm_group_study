# # 박윤지
# def select(e, cnt):  # e: 종료시간, cnt = 수행한 스케줄수
#     if e >= 24:
#         return cnt
#     minE = 25  # 24보다 큰 수
#     minIdx = N  # idx는 N-1 까지이므로 N으로 설정
#     for i in range(0, N):
#         if sche[i][0] >= e:
#             if minE > sche[i][1]:
#                 minE = sche[i][1]
#                 minIdx = i
#     if minIdx == N:  # 쓸 스케줄이 없어서 minIdx가 갱신되지 않았으면 cnt 리턴
#         return cnt
#     else:
#         sche[minIdx] = [0, 0]  # 쓴 스케줄 앞으로 못쓰도록 내용 바꾸기
#         return select(minE, cnt+1)
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     sche = [list(map(int, input().split())) for _ in range(N)]
#     # 종료 시간이 가장 작은 스케줄을 하나 잡음
#     # 앞 종료시간보다 시작시간이 같거나 크면서, 종료시간이 가장 작은 스케줄 선택
#     # 선택할 것이 없을 때까지 반복
#     print('#{} {}'.format(tc, select(0, 0)))

#김정빈
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    times = [list(map(int, input().split())) for _ in range(N)]
    times.sort(key=lambda x: (x[1]))  # sort하면 시작 값을 기준으로 정렬되므로
    end = times[0][1]
    cnt = 1
    for i in range(1, N):
        if times[i][0] >= end:
            end = times[i][1]
            cnt += 1
    print('#{} {}'.format(tc, cnt))
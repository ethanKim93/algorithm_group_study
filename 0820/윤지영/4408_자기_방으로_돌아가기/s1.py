# [0] * 400 만들어서, 1-> 4면 1번부터 4번까지 1 추가 , 3->6번까지 가면, 3번부터 6번까지 1추가 .. 반복하면 겹치는 부분은 그만큼 가야하는 것이므로
# 이 배열의 최대값을 구하면 그게 최소시간일 것?

# 아니면 홀수/짝수 나눠서, 1,3,5 = > 1,2,3인덱스로 바꾸고, 2,4,6 = > 1,2,3인덱스로 바꾸고 등등으로 해서 하나의 배열로 만들고,
# # 겹치는 부분 찾아서 위와 같이 구하기
# 반례 4 (1,400), (400,1), (200,400), (300,100)
# 배열 400개로 무작정하면 반례-> 2 (1,3) ,(4,6) 이 답이 2여야하는데 1나옴

import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1,T+1):
    N = int(input())    # 학생 수
    room = [0] * 201    # 방복도 배열
    for _ in range(N):
        a, b = map(int,input().split())
        if a > b :
            a,b = b,a
        if a % 2 :
            a += 1
        if b % 2 :
            b += 1
        a,b = a//2, b//2
        for k in range(a,b+1):
            room[k] += 1
    time = room[1]
    for i in range(1, 201):
        if room[i] > time:
            time = room[i]
    print('#{} {}'.format(tc, time))






# for tc in range(1,T+1):
#     N = int(input())    # 학생 수
#     room = [0] * 401    # 방복도 지나간 수 배열
#     for _ in range(N):
#         a, b = map(int,input().split())
#         if a > b :
#             a,b = b,a
#         for k in range(a,b+1):
#             room[k] += 1
#     time = room[0]
#     for i in range(401):
#         if room[i] > time:
#             time = room[i]
#     print('#{} {}'.format(tc, time))


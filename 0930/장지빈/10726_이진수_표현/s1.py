# import sys
# sys.stdin = open('input.txt')
#
# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     flag = True
#     M = format(M, 'b')
#
#     if len(M) < N:
#         flag = False
#     else:
#         for i in range(len(M)-1, len(M)-N-1, -1):
#             if not int(M[i]):
#                 flag = False
#                 break
#
#     if flag:
#         flag = 'ON'
#     else:
#         flag = 'OFF'
#     print('#{} {}'.format(tc, flag))
import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    bitN = (2**N) - 1                   # N개의 비트가 켜져있다는것은 2^N에서 1을 뺀것과 같은의미
    answer = 'OFF'
    if M & bitN == bitN:                # bitN의 모든 비트가 M에 포함되어 있을 때(마지막 N개의 비트가 모두 켜져있을 때)
        answer = 'ON'                   # ON
    print('#{} {}'.format(tc, answer))
# 진석님 코드
# n이 3일땐 111, 4일땐, 1111와 같은 식으로 간다. 2의 n제곱 -1 -> n=3 -> 2^n-1 = 7 = (111){2} / n=4 -> 2^n-1 = 15 = (1111){2}
# & 연산을 하게 되면 M에 어떤 값이 들어가더라도 마지막 n개 만큼의 비트를 &연산해서 켜져있으면(1이면) 1을 내려주고 다르면 0
# ex) M = 30 -> 11110 / N = 4 -> 2**n -1 [7]의 2진수 -> 1111 / &연산하게 되면 M&N -> (1 1 1 1 0 ) & ( 0 1 1 1 1 ) 이 bitN 과 같아야한다.
# (자리에 맞는 값이 둘 다 1이어야 한다.) 같다면 켜져있는 것으로 간주.
# 다른 True False 문제에도 적용 가능하다.
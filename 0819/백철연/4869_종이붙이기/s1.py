import sys
sys.stdin = open('sample_input.txt')

# T = int(input())
# for sq in range(T):
#     N = int(input())
#     print(N)
#     rec = 0
#     result = 0
#     if N % 20:
#         # 정사각형이 1개 일때
#         # (2(가로로 자른모양+사각형모양) * 직사각형의 개수)*대칭 + 1(전부 직사각형 모양일때는 중복)
#         rec = int((N - 20) / 10)
#         result = (2 * rec)*2 + 1
#     # 정사각형이 2개 이상일때
#
#     else:
#         pass
#     print(result)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    p = 1
    n = N//10
    for i in range(1, n+1):
        if i%2:
            p = (p*2) - 1
        else:
            p = (p*2) + 1
    print('#{} {}'.format(tc, p))
import sys
sys.stdin = open("sample_input.txt")

# 점화식 an = an-2 * 2 + an-1
T = int(input())


def check(K):
    m = K//10
    li = [0] * (m+1)
    li[0], li[1] = 1, 3
    for k in range(2, m):
        li[k] = li[k-2] * 2 + li[k-1]
    return li[m-1]


for tc in range(1,T+1):
    N = int(input())
    result = check(N)
    print('#{} {}'.format(tc, result))


# # a3 = a2 * 2 - 1
# # a4 = a3 * 2 + 1
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     p = 1
#     num = N//10
#     for i in range(1, num+1):
#         if i % 2 :
#             p = (p*2) - 1
#         else:
#             p = (p*2) + 1
#     print('#{} {}'.format(tc, p))

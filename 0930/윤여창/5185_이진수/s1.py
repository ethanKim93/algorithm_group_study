import sys
sys.stdin = open("sample_input.txt")
#
# T = int(input())
#
# patt = {
#     'A': 10,
#     'B': 11,
#     'C': 12,
#     'D': 13,
#     'E': 14,
#     'F': 15
#     }
#
# for tc in range(1, T+1):
#     N, N_16 = input().split()
#     ans = ''
#     for i in N_16[::-1]:
#         if i in patt:
#             i = patt[i]
#         else:
#             i = int(i)
#         for _ in range(4):
#             ans = str(i % 2) + ans
#             i //= 2
#
#     print("#{} {}".format(tc, ans))



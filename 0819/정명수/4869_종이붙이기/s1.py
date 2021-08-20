import sys
sys.stdin = open("input.txt")

# T = int(input())
# for test_case in range(1,T+1):
#     N = int(input())
#     box = []
#     counter = 0
#     i = 0
#     while i < N//10:
#         if sum(box) < N:
#             box.append(10)
#         elif sum(box) == N:
#             counter += 1
#             for j in box:
#                 if j == 20:
#                     counter += 1
#             box.pop()
#             box.pop()
#             box.append(20)
#         i += 1
#
#     print(counter)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    p = 1
    n = N//10
    for i in range(1, n+1):
        if i%2:
            p = (p*2)-1
        else:
            p = (p*2)+1
    print('#{} {}'.format(tc,p))



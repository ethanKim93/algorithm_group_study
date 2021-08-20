import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    N, strr = input().split()
    #print(N, strr)
    bin_list = []
    bin_list.append('A')
    for x in strr:
        if x != bin_list[-1]:
            bin_list.append(x)
        else:
            bin_list.pop()
    #print(bin_list)
    print('#{} {}'.format(tc, ''.join(bin_list[1:])))

# #16 4100112380990844
# for tc in range(1, 11):
#     N, P = input().split()
#     N = int(N)
#     stack = []
#     for i in range(N):
#         if not stack:
#             stack.append(P[i])
#         else:
#             if stack[-1] == P[i]:
#                 stack.pop()
#             else:
#                 stack.append(P[i])
#     print('#{}'.format(tc), end=' ')
#     print(''.join(stack))
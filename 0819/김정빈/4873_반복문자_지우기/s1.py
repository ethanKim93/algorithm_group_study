import sys
sys.stdin = open("input.txt")
#풀이1
def remov(N):
    i = 0
    while i < len(N)-1:
        if N[i] == N[i+1]:
            N.pop(i)
            N.pop(i)
            remov(N)
        else:
            i+=1
    return len(N)

T = int(input())
for tc in range(1, T+1):
    N = list(input())
    print('#{} {}'.format(tc, remov(N)))

#풀이2
# T = int(input())
# for tc in range(1, T+1):
#     N = list(input())
#     ans = []
#     for n in N:
#         if not ans:
#             ans.append(n)
#         elif n == ans[-1]:
#            ans.pop(-1)
#         else:
#             ans.append(n)
#     print('#{} {}'.format(tc, len(ans)))
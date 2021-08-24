import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def winner(l,r):
    if (tournament[l] - tournament[r])%3 < 2:
        return l
    return r

def vs(start, end):
    left = vs(start, (start+end)//2)
    right = vs((start+end)//2+1, end)
    return winner(left, right)


for tc in range(1, T+1):
    N = int(input())
    tournament = list(map(int, input().split()))

    vs(1, N)

# def rsp(x, y):
#     if (num[x-1] == 1 and num[y-1] == 3) or (num[x-1] == 1 and num[y-1] == 1):
#         return x
#     elif (num[x-1] == 2 and num[y-1] == 1) or (num[x-1] == 2 and num[y-1] == 2):
#         return x
#     elif (num[x-1] == 3 and num[y-1] == 2) or (num[x-1] == 3 and num[y-1] == 3):
#         return x
#     return y
#
# def recu(i,j) :
#     if i == j :
#         return i
#     first = recu(i, (i+j)//2)
#     last = recu((i+j)//2+1, j)
#     return rsp(i, j)
#
# T = int(input())
#
# for tc in range(T, T+1):
#     N = int(input())
#     num = list(map(int,input().split()))
#     i = 1
#     j = N
#
#     print('#{} {}'.format(tc, recu(i,j)))


print(-2 //3)





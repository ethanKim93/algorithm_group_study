import sys
sys.stdin=open('input.txt')
# def binarycac(N):
#     global M
#     for i in range(N):
#         if not M%2:
#             return False
#         M=M//2
#     else:
#         return True
#
# T=int(input())
# for tc in range(1,T+1):
#     N,M=map(int,input().split())
#     result = binarycac(N)
#     if result:
#         print('#{} ON'.format(tc))
#     else:
#         print('#{} OFF'.format(tc))
def findmatch():
    for i in range(N):
        if M & (1<<i):
            return True
        else:
            return False

T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    result=''
    result=findmatch()
    if result:
        print('#{} ON'.format(tc))
    else:
        print('#{} OFF'.format(tc))
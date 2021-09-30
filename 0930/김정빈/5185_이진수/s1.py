import sys
sys.stdin = open("input.txt", "r")
#5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수
def binary(n10):
    for i in range(4):
        if n10 & (8>>i):
            print('1',end="")
        else:
            print('0',end="")

T = int(input())
for tc in range(1, T+1):
    N, n16 = input().split()
    print('#{}'.format(tc),end=" ")
    for i in range(0, int(N)):
        n10 = int(n16[i], 16)
        binary(n10)
    print()
    # print('#{} {}'.format(tc, bin(int(n16,16))[2:].zfill(int(N)*4)))
    print(bin(n10))
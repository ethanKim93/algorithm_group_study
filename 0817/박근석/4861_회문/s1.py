import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    list_a = [0]*N
    for i in range(len(list_a)):
        list_a[i] = list(input().split())

    count = 0
    for i in range(N):
            for j in range(N-M+1):
                list_a[i][j:j+M] == list_a[i][j:j+M][::-1]
                result = list_a[i][j:j+M]
                break



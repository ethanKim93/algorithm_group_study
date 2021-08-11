import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    A = [0]*5
    for i in range(5):
        A[i] = list(map(int, input().split()))

    sum = 0

    for i in range(5):
        for j in range(5):
            if 0 <= i < 5 and 0 <= j - 1 < 5:
                sum += abs(A[i][j] - A[i][j-1])
            if 0 <= i < 5 and 0 <= j + 1 < 5:
                sum += abs(A[i][j] - A[i][j+1])
            if 0 <= i - 1 < 5 and 0 <= j < 5:
                sum += abs(A[i][j] - A[i-1][j])
            if 0 <= i + 1 < 5 and 0 <= j < 5:
                sum += abs(A[i][j] - A[i+1][j])
            print(sum)
    print(sum)
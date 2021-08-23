import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    M = list(map(int, input().split()))[::-1]
    count = 0
    max = M[0]
    for i in M:
        if i > max:
            max = i
        else:
            count += max - i

    print(count)




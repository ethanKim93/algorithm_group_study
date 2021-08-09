import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    L = int(input())
    builds = list(map(int, input().split()))

    # print(L)
    # print(builds)
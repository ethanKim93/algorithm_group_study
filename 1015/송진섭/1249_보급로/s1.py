import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    map_info = [list(map(int, input())) for _ in range(N)]
    # print(map_info)
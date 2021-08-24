import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) #돌아가야 할 학생들의 수

    routes = [list(map(int, input().split())) for _ in range(N)]
    print(routes)
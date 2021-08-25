import sys

sys.stdin = open('sample_input.txt')


def vs(start, end):
    left = vs(start, (start + end) // 2)  # 왼쪽그룹
    right = vs((start + end) // 2, end)  # 오른쪽그룹


for tc in range(1, int(input()) + 1):
    N = int(input())
    tournament = list(map(int, input().split()))

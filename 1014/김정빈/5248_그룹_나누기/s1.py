import sys
sys.stdin = open("input.txt")
#5248. [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기
"""
상호배타집합표현 / DFS 두가지 방법
"""
def dfs():


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    apps = list(map(int, input().split()))
    visited = [0]*(N+1)
    cnt = 0

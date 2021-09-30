"""
#1 38
#2 48
"""
from pprint import pprint
import sys
sys.stdin = open("input.txt")
#1242. [S/W 문제해결 응용] 1일차 - 암호코드 스캔
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = set([input().strip('0') for _ in range(N)])
    lines = []
    for line in arr:
        if line != '':
            lines.append(bin(int(line, 16))[2:])
    print(lines)

"""
주호님 설명
일단 이진수로 바꿔
"""
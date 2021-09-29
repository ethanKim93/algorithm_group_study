import sys
sys.stdin = open("sample_input.txt")
#상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
tunnel = [
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 1, 0],
]
for tc in range(1, int(input())+1):
    pass

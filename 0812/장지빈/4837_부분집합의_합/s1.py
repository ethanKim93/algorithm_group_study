import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    elm = [i for i in range(1, 13)]
    lenelm = len(elm)
    ls = []

    for i in range(1 << lenelm):
        pass

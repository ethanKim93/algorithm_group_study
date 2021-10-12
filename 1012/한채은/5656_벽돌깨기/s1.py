import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    '''
    N: 구슬 쏘는 횟수
    W, H : 벽돌 가로, 세로
    
    '''
    N, W, H = map(int, input().split())
    block = [list(map(int, input().split())) for _ in range(H)]


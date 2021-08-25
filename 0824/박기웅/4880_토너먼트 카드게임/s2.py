'''
후안 교수님 코드
'''
import sys
sys.stdin = open("sample_input.txt")

def winner(l, r):
    if (tournament[l] - tournament[r])%3 < 2: # 가위 바위 보가 1, 2, 3으로 주어졌을 경우
        return l
    return r
def vs(start, end):
    if start == end:
        return end
    left = vs(start, (start+end)//2)        #하나로 남을 때까지 재귀호출
    right = vs((start+end)//2+1, end)
    return winner(left, right)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tournament = [0]+list(map(int, input().split()))

    print('#{} {}'.format(tc, vs(1, N)))
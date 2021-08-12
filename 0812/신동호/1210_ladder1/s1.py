import sys
sys.stdin = open('input.txt')
def climb(ladders, long, stage, pos=0): # ladders는 남아있는 행렬, long은 전체 사다리 길이, stage는 현재 층 row, pos는 현재 위치 col
    if long == len(ladders): # 남은 행렬 길이가 전체 사다리와 같음
        for ind in range(len(ladders[-1])):
            if ladders[-1][ind] == 2: # 도착점 찾기
                return climb(ladders[:-1], long, stage-1, ind) # 도착점 바로 위 지점에서 재귀

    if stage == 0: # 맨 위에 도달
        return pos # 시작점 반환

    if pos >= 1 and ladders[-1][pos-1]: # 왼쪽에 최소 한 칸 있고, 왼쪽이 1
        for ind in range(pos-1,-1,-1): # 오른쪽에서 왼쪽으로
            if ladders[-1][ind]: # 왼쪽으로 계속 감
                pass
            else: # 0 만남
                return climb(ladders[:-1], long, stage-1, ind+1) # 0을 만나기 전 지점 위에서 재귀
        else:
            return climb(ladders[:-1], long, stage-1, ind) # 벽과 만난 지점 위에서 재귀

    elif pos <= len(ladders[-1])-2 and ladders[-1][pos+1]: # 오른쪽에 최소 한 칸 있고, 오른쪽이 1
        for ind in range(pos+1,len(ladders[-1])): # 왼쪽에서 오른쪽으로
            if ladders[-1][ind]: # 오른쪽으로 계속 감
                pass
            else: # 0 만남
                return climb(ladders[:-1], long, stage-1, ind-1) # 0을 만나기 전 지점 위에서 재귀
        else:
            return climb(ladders[:-1], long, stage-1, ind) # 벽과 만난 지점 위에서 재귀
    else:
        return climb(ladders[:-1], long, stage - 1, pos) # 위로 올라가며 바로 위 지점에서 재귀

T = 10

for tc in range(1, T+1):
    N = int(input())
    ladders = [list(map(int, input().split())) for _ in range(100)]
    print('#{} {}'.format(tc,climb(ladders, len(ladders),len(ladders)))) # climb으로 재귀 돌리기, 시작할 때 전체 사다리 길이와 현재 층은 같다
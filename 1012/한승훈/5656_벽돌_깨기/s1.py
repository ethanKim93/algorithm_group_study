import sys
sys.stdin = open('sample_input.txt')
import copy

def back(n,lst):
    global min_cnt

    if crush(lst):
        min_cnt = 0
        return

    # 남은 횟수가 0일때
    if n == 0:
        cnt = 0
        for i in range(W):
            for j in range(H):
                if lst[j][i]:
                    cnt += 1
        min_cnt = min(cnt, min_cnt)
        return

    for u in range(W):
        temp = copy.deepcopy(lst)
        for z in range(H):
            if temp[z][u]:
                bomb(z, u, temp[z][u], temp)
                rearrange(temp)
                back(n-1, temp)
                temp = copy.deepcopy(lst)
                break



# 폭파
def bomb(x,y,n,lst):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    lst[x][y] = 0
    for i in range(4):
        for j in range(1, n):
            nx, ny = x+dx[i]*j, y+dy[i]*j
            if 0 <= nx < H and 0 <= ny < W and blocks[nx][ny] >= 1:
                if lst[nx][ny] > 1:
                    bomb(nx, ny, lst[nx][ny],lst)
                lst[nx][ny] = 0


# 폭파 후 재배치
def rearrange(lst):
    for a in range(W):
        for i in range(H - 1, -1, -1):
            if not lst[i][a]:
                for j in range(i, -1, -1):
                    if lst[j][a]:
                        lst[i][a] = lst[j][a]
                        lst[j][a] = 0
                        break

# 부실것이 없는지 확인하는 코드
def crush(lst):
    a = 0
    for i in range(H):
        a += sum(lst[i])
    if not a:
        return True


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    blocks = [list(map(int, input().split())) for _ in range(H)]
    min_cnt = 10000000
    back(N, blocks)
    print('#{} {}'.format(tc,min_cnt))




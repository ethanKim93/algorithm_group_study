import sys
sys.stdin = open('input.txt')

T = int(input())
# 달팽이 적용 함수
def roll(size):
    box = [[1]*(size+2),*[[1,*([0]*size),1] for _ in range(size)],[1]*(size+2)] # 원래 리스트 주변에 1로 1만큼 패딩된 리스트
    x = y = 1
    dx = [0, 1, 0, -1] # 우 하 좌 상
    dy = [1, 0, -1, 0]
    mode = 0
    for num in range(1, size ** 2 + 1): # 넣을 숫자들
        box[x][y] = num
        if mode == 0 and box[x+dx[mode]][y+dy[mode]]: # 1로 패딩된 벽이나 이미 값이 입력된 0이 아닌 요소를 만났을 때 방향 전환
            mode = 1
        elif mode == 1 and box[x+dx[mode]][y+dy[mode]]:
            mode = 2
        elif mode == 2 and box[x+dx[mode]][y+dy[mode]]:
            mode = 3
        elif mode == 3 and box[x+dx[mode]][y+dy[mode]]:
            mode = 0
        x, y = x + dx[mode], y + dy[mode] #mode가 바뀔 때마다 다음 이동 방향 정해짐
    snail = [x[1:-1] for x in box[1:-1]] #주변의 1 패딩 없애기
    return(snail)

for tc in range(1, T+1):
    size = int(input())
    print('#{}'.format(tc))
    snail = roll(size)
    for i in snail:
        print(' '.join(map(str,i)))


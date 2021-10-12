import sys
sys.stdin = open('sample_input.txt')

def clearvisited():
    for i in range(101):
        visited[i] = False

def solve():
    global maxV
    for i in range(N-1):
        for j in range(N-1):
            for a in range(1, N-1):
                for b in range(1, N-1):
                    clearvisited()

                    # i, 1에서 시작하여 a, b의 크기를 갖는 사각형을 가정
                    curX = j
                    curY = i
                    isError = False
                    # 우상으로 a만큼 이동하면서 가능한지 확인한다.
                    for k in range(a):
                        curX += 1
                        curY -= 1
                        if curX >= N or curY < 0 or visited[data[curY][curX]]:
                            isError = True
                            break
                        else:
                            visited[data[curY][curX]] = True
                    if isError:  # 에러 발생시
                        continue
                    # 우하로 b만큼 이동하면서 가능한지 확인
                    for k in range(b):
                        curX += 1
                        curY += 1
                        if curX >= N or curY >= N or visited[data[curY][curX]]:
                            isError = True
                            break
                        else:
                            visited[data[curY][curX]] = True
                    if isError:  # 에러 발생시
                        continue
                    # 좌하
                    for k in range(a):
                        curX -= 1
                        curY += 1
                        if curX < 0 or curY >= N or visited[data[curY][curX]]:
                            isError = True
                            break
                        else:
                            visited[data[curY][curX]] = True
                    if isError:  # 에러 발생시
                        continue
                    # 좌상
                    for k in range(b):
                        curX -= 1
                        curY -= 1
                        if curX < 0 or curY < 0 or visited[data[curY][curX]]:
                            isError = True
                            break
                        else:
                            visited[data[curY][curX]] = True
                    if isError:  # 에러 발생시
                        continue

                    # 최대 길이를 계산한다
                    if (a+b)*2 > maxV:
                        maxV = (a+b)*2

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * 101 # 디저트 종류는 100개지만 인덱스 1부터 사용하려고
    maxV = -1
    solve()
    print('#{} {}'.format(test_case, maxV))
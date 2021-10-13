import sys
sys.stdin = open('sample_input.txt')

# 반복문 이용
def solve():
    global maxV
    for i in range(N-1):
        for j in range(N-1):
            for a in range(1, N-1):
                for b in range(1, N-1):

                    # i, j에서 시작하여 a, b의 크기를 갖는 사각형
                    curX = j
                    curY = i
                    visited = [False] * 100
                    isError = False
                    # 우측 위로 a만큼 이동하면서 가능한지 체크
                    for k in range(a):
                        curX += 1
                        curY -= 1
                        # 오류 발생, 이미 나온 숫자인지도 체크해야함(visited)
                        if curX >= N or curY < N or visited[arr[curY][curX]]:
                            isError = True
                            break
                        else:
                            visited[arr[curY][curX]] = True
                    if isError:
                        continue
                    # 우측 아래로 b만큼 이동하면서 가능한지 체크
                    for k in range(a):
                        curX += 1
                        curY += 1
                        # 오류 발생, 이미 나온 숫자인지도 체크해야함(visited)
                        if curX >= N or curY >= N or visited[arr[curY][curX]]:
                            isError = True
                            break
                        else:
                            visited[arr[curY][curX]] = True
                    if isError:
                        continue
                    # 촤하
                    for k in range(a):
                        curX -= 1
                        curY += 1
                        # 오류 발생, 이미 나온 숫자인지도 체크해야함(visited)
                        if curX < 0 or curY >= N or visited[arr[curY][curX]]:
                            isError = True
                            break
                        else:
                            visited[arr[curY][curX]] = True
                    if isError:
                        continue
                    # 좌상
                    for k in range(a):
                        curX -= 1
                        curY -= 1
                        # 오류 발생, 이미 나온 숫자인지도 체크해야함(visited)
                        if curX < 0 or  curY < 0 or visited[arr[curY][curX]]:
                            isError = True
                            break
                        else:
                            visited[arr[curY][curX]] = True
                    if isError:
                        continue

                    # 길이 계산
                    if (a+b) * 2 > maxV:
                        maxV = (a+b) * 2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    solve()
    print('#{} {}'.format(tc, maxV))
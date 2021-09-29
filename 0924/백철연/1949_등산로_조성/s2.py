
import sys
sys.stdin = open('sample_input.txt')
#
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# def work()




T = int(input())
for tc in range(1,11):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 가장 높은 봉우리 찾기

    max_list = []
    maxV = 0
    visited = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            if maxV <= arr[i][j]:
                maxV = arr[i][j]
                max_list.append((i,j))
                if maxV < arr[i][j]:
                    max_list = []
                    max_list.append((i,j))
    print(max_list)



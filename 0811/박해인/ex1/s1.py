import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = M = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    # 두번째 세번째 줄의 input을 하나의 list로 묶기
    # for _ in range(N) 단순 반복을 할 때는 이 형태 많이 씀

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j]
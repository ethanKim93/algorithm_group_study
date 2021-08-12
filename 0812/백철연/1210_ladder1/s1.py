import sys
sys.stdin = open('input.txt')



for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    print(arr)
    # 도착지점의 column index 찾기
    for c in range(100):
        if arr[99][c] == 2:
            break
    # 도착지점에서 거꾸로 올라가기



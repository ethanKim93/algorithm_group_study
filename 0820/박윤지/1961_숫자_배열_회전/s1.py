import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    # 90도 회전
    arr90 = []
    for j in range(N):
        num = ''
        for i in range(N-1, -1, -1):
            num += str(arr[i][j])
        arr90.append(num)
    # 180도 회전
    arr180 = []
    for i in range(N-1, -1, -1):
        num = ''
        for j in range(N-1, -1, -1):
            num += str(arr[i][j])
        arr180.append(num)
    # 270도 회전
    arr270 = []
    for j in range(N-1, -1, -1):
        num = ''
        for i in range(N):
            num += str(arr[i][j])
        arr270.append(num)
    # 3 각도 섞기
    print('#{}'.format(tc))
    for n in range(N):
        print('{} {} {}'.format(arr90[n], arr180[n], arr270[n]))


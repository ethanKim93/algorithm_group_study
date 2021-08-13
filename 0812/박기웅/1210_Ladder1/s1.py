import sys
sys.stdin = open("input.txt")

for _ in range(10):
    T = int(input())
    #양 사이드 0 패딩 추가 좌 혹은 우로 빠지는 경우 없애기 위함
    arr = [[0]+list(map(int, input().split()))+[0] for _ in range(100)]
    # 도착지점 찾기
    for i, a in enumerate(arr[-1]):
        if a == 2:
            j = i
    #상, 좌, 우
    di = [-1, 0, 0]
    dj = [0, -1, 1]
    # 현재 방향 표시 변수
    k = 0

    i = 99
    while(i):
        #현재 방향대로 움직이기
        i += di[k]
        j += dj[k]
        #현재 방향에서 좌, 우 확인
        if k: #현재 방향이 좌 혹은 우 방향 인경우
            if arr[i-1][j]: #상방향에 1이 있으면 일단 방향 상쪽으로
                k = 0
            #상방향이 없다면 그대로 가야지..
        else: #현재 방향이 상방향 이라면 -> 좌, 우 확인 해야지..
            if arr[i][j-1]: #좌방향에 1이면
                k = 1
            if arr[i][j+1]: #우방향에 1이면
                k = 2
    start = j-1 #양 사이드에 패딩 추가했으므로

    print('#{} {}'.format(T, start))






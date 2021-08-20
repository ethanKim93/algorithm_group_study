import sys
sys.stdin = open("input.txt")

for tc in range(1,11):
    tc,case_len = map(int,input().split())
    mat = [[0]*100 for _ in range(100)]
    visit = [0]*100
    str_list = list(map(int,input().split()))


    # 저장 방법
    #1.ch1 ,ch2
    ch1 = [0]*100
    ch2 = [0] * 100

    for i in range(N):
        if ch1[road[2*i]] == 0:
            ch1[road[2*i]] = road[2*i+1]
        else:
            ch2[road[2*i]] = road[2*i+1]

    #2. 인접 행렬 방식
    adj_arr = [[0]*100 for _ in range(100)]
    for i in range(N):
        adj_arr[road[2*i]][road[2*i+1]] = 1


    #3. 인접 리스트
    adj_list = [[] for _ in range(100)]
    for i in range(N):
        adj_list[road[2 * i]].append(road[2 * i + 1])


    # 반복 구조로 만들어보자!

    if visited

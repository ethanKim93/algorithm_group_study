import sys
sys.stdin = open("sample_input.txt")

for tc in range(1, int(input())+1):
    N = int(input())
    step = [0] * 200                    #중앙 복도 카운트배열
    cnt = 0
    for _ in range(N):
        s, e = map(int, input().split())
        if s == e:                      # 출발지와 도착지 같은 경우 아무 흔적도 안남김
            continue
        if s > e:                       # 출발지가 도착지보다 큰 경우 바꿔줌
            s, e = e, s
        si = s//2 if s%2 else s//2 -1   # 짝수인 경우 s: 10 -> idx: 4, 홀수인 경우 s: 9 -> idx: 4
        ei = e//2 if e%2 else e//2 -1

        for i in range(si, ei+1):       # 흔적을 지나면 1씩 카운팅
            step[i] += 1

    maxh = 0                            # 가장 큰 흔적개수가 오래걸린 시간
    for h in step:
        if maxh < h:
            maxh = h
    print('#{} {}'.format(tc, maxh))
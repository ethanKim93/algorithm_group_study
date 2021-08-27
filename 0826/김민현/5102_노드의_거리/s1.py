import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1,T+1):
    V,E = map(int,input().split())
    edge =list([] for _ in range(V+1))
    for _ in range(E): #인접리스트로 받기
         i, j = map(int, input().split())
         edge[i].append(j)
         edge[j].append(i)
    S,G = map(int, input().split())

    q = []
    visit = [0]*(V+1) #방문 여부 확인 및 거리 계산 리스트
    start = S #초기 start값
    flag = 1 # G 일치여부 확인 flag
    while True: #항상 반복 실행 (Q가 비었거나,G에 도달하면 flag를 이용해 break)
        for i in edge[start]:
            if visit[i] == 0:
                q.append(i)
                visit[i] = visit[start]+ 1 #거리값 계산
                if i == G: # 목표 노드에 도착하면
                    flag = 0
                    break
        if not q or not flag: #q가 비었거나, flag가 0이면(목표노드에 도착했으면)
            break
        start = q.pop(0)#q에 맨 앞값 반환

    print('#{} {}'.format(tc,visit[G]))

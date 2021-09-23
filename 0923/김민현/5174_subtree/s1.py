import sys
sys.stdin = open("sample_input.txt")

T = int(input())

def nodeCnt(n):
    global cnt
    cnt += 1 #노드 갯수 카운트
    if nodes[n]:
        visit[n] = 1 # 방문기록 남기기
        for num in nodes[n]:
            if not visit[num]:
                nodeCnt(num) # 재귀함수 호출


for tc in range(1,T+1):
    cnt = 0
    data = list(map(int,input().split()))
    E,N = data[0],data[1]
    node_data = list(map(int,input().split()))
    nodes = [[] for _ in range(E+2)]
    visit = [0] * (E+2) #방문한 노드
    for i in range(0,len(node_data)-1,2):
        nodes[node_data[i]].append(node_data[i+1])
    nodeCnt(N) # 함수 호출
    print('#{} {}'.format(tc, cnt))

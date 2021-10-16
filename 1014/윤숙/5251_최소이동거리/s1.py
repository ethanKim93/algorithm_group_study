
'''
실패...
원인은 크루스칼을 오해하고 문제를 접근
크루스칼을 공부하고 문제를 접근하려 했으나 답이 안나왔다.
출발점이 정해져 있는 경우 크루스칼이 아닌 다익스트라로 풀어야함
최소 신장 트리를 찾을 때는 크루스칼..
점과 점 사이의 거리를 구할 때는 다익스트라..
임의의 두점 간의 최소 거리를 구할 때 사용 -> 다익스트라

최소 비용으로 모든 점을 다 이을 때 사용된다.
다만, 모든 점을 다이은 경우 최소 비용이라 말할 수 있다.
그렇지만 임의의 두점 간 거리가 최소라는 보장은 없다. -> 크루스칼
'''

import sys

sys.stdin = open('input.txt')
def find(x):
    if visited[x]!=x:

        return find(visited[x])
    else:
        return x
def union(x,y):
    if find(x)<find(y):
        visited[find(y)]=find(x)
    else:
        visited[find(x)] = find(y)

T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())  # 마지막 연결지점 번호 N, 도로의 개수 E
    visited=[i for i in range(E)]
    tmp=[]
    for _ in range(E):
        p1, p2, w = map(int, input().split())  # 시작, #끝 , #가중치
        tmp.append([w,p1,p2])
    tmp.sort()
    cnt=0
    total=0
    for w,p1,p2 in tmp:
        if find(p1)!=find(p2):
            cnt+=1
            total+=w
            union(p1,p2)
        if cnt == E:
            break
    print(visited)
    print(total)




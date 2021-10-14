import sys
sys.stdin = open('input.txt')

li = list(map(int,input().split()))
adj_list = [[] for _ in range(10)]
visited = [0]*10
for i in range(0,len(li),2):
    adj_list[li[i]].append(li[i+1])
    adj_list[li[i+1]].append(li[i])
q = [1]
while q:
    t = q.pop()
    if not visited[t]:
        print(t,end=" ")
        visited[t] = 1
    for i in adj_list[t]:
        if not visited[i]:
            q.append(i)
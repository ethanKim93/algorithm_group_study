import sys
sys.stdin = open('input.txt')

V = int(input())
E_li = list(map(int, input().split()))

left = [0]*(V+1)
right = [0]*(V+1)

for i in range(len(E_li)//2):
    v1, v2 = E_li[2*i], E_li[2*i+1]
    if left[v1] == 0:
        left[v1] = v2
    else:
        right[v1] = v2

stack =[1]
visited = [0] * (V+1)
turn = []

while stack:
    t = stack.pop(0)
    visited[t] = 1
    turn.append(t)

    if right[t] and not visited[right[t]]:
        # stack.append(right[t])


    if left[t] and not visited[left[t]]:
        stack.insert(0, left[t])


print(turn)
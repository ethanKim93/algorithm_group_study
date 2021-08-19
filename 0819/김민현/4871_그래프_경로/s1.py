#김민현
import sys
sys.stdin = open("sample_input .txt")

for tc in range(1,int(input())+1):
    V,E = map(int,input().split())
    mat = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        nod_start,nod_end = map(int, input().split())
        mat[nod_start][nod_end] = 1
       # mat[nod_end][nod_start] = 1#일방향이기 때문에 하면 안됨
    start,end = map(int, input().split())

    stack = [start]
    i = 0
    result = 0
    visited=[0]*(V+1)
    while i < V+1:
        visited[start] = 1
        if mat[start][i] == 1 and visited[i] != 1:
            if i == end:
                result = 1
                break
            else:
                stack.append(i)
                start = i
                visited[i] = 1
                i = 1
        elif i == V:
            if len(stack) != 0:
                start = stack.pop(-1)
                i = 0
            else:
                result = 0
                break
        else:
            i += 1

    print('#{} {}'.format(tc,result))


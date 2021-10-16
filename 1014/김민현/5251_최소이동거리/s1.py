import sys
sys.stdin = open('sample_input.txt')

def find(v,dis = 0):
    for end in arr[v]:
        if end:
            find(end,)

T = int(input())

for tc in range(1,T+1):
    N,E = map(int,input().split())
    arr = [[0]*E for _ in range(E)]

    for i in range(E):
        start,end,dis = map(int,input().split())
        arr[start][end] = dis
    find(0)
    print("#{} {}".format(tc,arr))
import sys
sys.stdin = open("input.txt")
T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    arr_1=[[0]*N for _ in range(N)]
    arr_2=[[0]*N for _ in range(N)]
    arr_3=[[0]*N for _ in range(N)]
    print("#{}".format(test_case))
    for i in range(N):
        for j in range(N):
            arr_1[i][j]=arr[N-1-j][i]
            arr_2[i][j]=arr[N-1-i][N-1-j]
            arr_3[i][j]=arr[j][N-1-i]
    for i in range(N):
        for j in range(N):
            print(arr_1[i][j],end="")
        print(end=" ")
        for j in range(N):
            print(arr_2[i][j],end="")
        print(end=" ")
        for j in range(N):
            print(arr_3[i][j],end="")
        print()
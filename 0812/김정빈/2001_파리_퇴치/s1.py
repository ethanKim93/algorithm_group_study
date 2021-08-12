import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    fly = []
    for i in range(N): #arr를
        for j in range(N):
            for x in range(M): #M씩만큼 돌아야 하는데...
                for y in range(M):
                    print(arr[x][y], end=",")
            print()
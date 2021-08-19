import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    V, E = map(int,input().split())
    arrs = []
    for i in range(E):
        n1, n2 = map(int, input().split())
        arrs.append([n1,n2])
    start, end = map(int, input().split())
#     route = []
#     for arr in arrs:
#         if arr[0] == start:
#             route.append(arr)
#         if arr[1] == end:
#             route.append(arr)

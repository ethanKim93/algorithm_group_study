import sys
sys.stdin = open("input.txt")
#1244. [S/W 문제해결 응용] 2일차 - 최대 상금
T = int(input())
for tc in range(1, T+1):
    arr, C = input().split()
    arr = list(arr)
    n = len(arr)
    print(arr)
    for i in range(n):
        mx = i
        for j in range(i, n):
            if



"""
123 1
2737 1
757148 1
78466 2
32888 2
777770 5
436659 2
431159 7
112233 3
456789 10
"""
"""
#1 321
#2 7732
#3 857147
#4 87664
#5 88832
#6 777770
#7 966354
#8 954311
#9 332211
#10 987645
"""
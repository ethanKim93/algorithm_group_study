#김민현
import sys
sys.stdin = open('input.txt')

dx = [-1,0,0]
dy = [0,-1,1]

dir = 0 # 0:위 ,1:좌 ,2:우

for i in range(1,11):
    tc = int(input())
    ladder = []
    for bar in range(100):
        arr = list(map(int,input().split()))
        ladder.append(arr)
    end_i = 0
    end_j = 0
    # 시작 위치값 찾기
    for i in range(len(ladder)):
        for j in range(len(ladder)):
            if ladder[i][j] == 2:
               end_i = i
               end_j = j
    x = end_j
    while x > 0:
        for i in range(len(ladder)):
            for j in range(len(ladder)):
                if ladder[i][j] == 2:
                end_i = i
                end_j = j
    print(end_j)
print()
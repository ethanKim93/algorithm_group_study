import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    width = int(input())
    heights = list(map(int, input().split()))
    max_grav = []
    bl = 0
    for i in range(width):
        for j in range(i+1,width):
            if heights[j]>=heights[i]:
                max_grav.append(j-i)
    print(max_grav)



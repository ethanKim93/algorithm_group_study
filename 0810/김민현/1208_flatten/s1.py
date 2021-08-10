import sys
sys.stdin = open('input.txt')


for tc in range(1,11):
    dump = int(input())
    heights = list(map(int,input().split()))

    for k in range(dump):
        heights[len(heights)-1] -= 1
        heights[0] += 1

        for i in range(len(heights)-1,0,-1):
            for j in range(0, i):
                if heights[j] > heights[j+1]:
                    heights[j],heights[j + 1] = heights[j + 1],heights[j]

    result =  heights[len(heights)-1] - heights[0]


    print('#{} {}'.format(tc,result))
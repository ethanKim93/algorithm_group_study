import sys

sys.stdin = open('input.txt')

T = int(input())
max_height = 100

#O(N^2) 풀이 방법
for tc in range(1, T+1) :
    width = int(input())
    heights = list(map(int, input().split()))
    heights.append(max_height)
    max_drop = 0
    for i in range(len(heights)) :
        temp_large = [i]
        for j in range(i + 1, len(heights)) :
            if heights[i] <= heights[j] :
                temp_large.append(j)
        temp_drop = temp_large[-1] - temp_large[0] + 1 - len(temp_large)
        if max_drop < temp_drop :
            max_drop = temp_drop

    print("#{} {}".format(tc, max_drop))


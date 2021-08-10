import sys
sys.stdin = open('input.txt')

def min_search():
    min_num = 987654321
    min_index = -1
    for i in range(len(height)):
        if height[i] < min_num:
            min_num = height[i]
            min_index = i
    return min_index

def max_search():
    max_num = -1
    max_index = -1
    for i in range(len(height)):
        if height[i] > max_num:
            max_num = height[i]
            max_index = i
    return max_index

for tc in range(1, 11):
    T = int(input())
    height = list(map(int, input().split()))

    for v in range(T):
        height[max_search()] -= 1
        height[min_search()] += 1

    print(height[max_search()] - height[min_search()])
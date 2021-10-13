# 안됨

import sys
sys.stdin = open('sample_input.txt')

xy = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def cross(a):
    global W
    global H
    print('? {}'.format(a))
    for q in range(a):
        print('?2 {}'.format(q))
        if a - q >= 0:
            arr[location[a]][a - q] = 0
        if a + q <= W - 1:
            arr[location[a]][a + q] = 0
        if a - q >= 0:
            arr[location[a - q]][a] = 0
        if a + q <= H - 1:
            arr[location[a + q]][a] = 0
    pass


T = int(input())
for tc in range(T):
    N, W, H = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(H))
    number = [0]*W
    locationx = [0]*W
    location = [0] * W
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != 0 and number[j] == 0:
                number[j] = arr[i][j]
                location[j] = i
    # print(arr)
    # print(number)
    # print(location)
    shoot = 0
    for k in range(len(number)):
        if number[k] > shoot:
            shoot = k
    # print(shoot)
    # print(arr[location[shoot]][shoot])
    cross(shoot)
    print(arr)
    print("end")
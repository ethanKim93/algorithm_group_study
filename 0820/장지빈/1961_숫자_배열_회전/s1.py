import sys
sys.stdin = open('input.txt')

def rotation90(arr):
    new_arr = [[0] * len(arr) for _ in range(len(arr))]
    a = 0
    for i in range(len(arr)-1, -1, -1):
        for j in range(len(arr)):
            new_arr[j][i] = arr[a][j]
        a += 1
    return new_arr


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]

    rot90 = rotation90(arr)
    rot180 = rotation90(rot90)
    rot270 = rotation90(rot180)

    print('#{}'.format(tc))
    for i in range(N):
        print(''.join(map(str, rot90[i])),  ''.join(map(str, rot180[i])), ''.join(map(str, rot270[i])))
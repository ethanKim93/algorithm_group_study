import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    while 1:
        for i in range(5):
            arr[0] -= i+1
            modify_arr = arr[1:]
            modify_arr.append(arr[0])
            arr = modify_arr
            if arr[-1] <=0:
                arr[-1] = 0
                cnt += 1
                break
        if cnt:
            break

    print("#{}".format(tc), end=' ')
    print(*arr)
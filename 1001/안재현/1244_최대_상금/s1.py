# 오류있음
import sys
sys.stdin = open('input.txt')


def Trans(lst):
    word = ''
    for q in range(len(lst)):
        word += str(lst[q])
        # print(word)
    return int(word)


def selection_sort2(arr, Lnum):
    global cnt
    # print(Lnum)
    # print(cnt)
    if cnt < Lnum:
        for i in range(len(arr)):
            tmp = 0
            Lamp = 0
            Atmp = 0
            for j in range(i, len(arr)):
                if arr[j] >= tmp:
                    tmp = arr[j]
                    Lamp = j
            print(Lamp)
            if arr[i] <= arr[Lamp]:
                Atmp = Trans(arr)
                arr[i], arr[Lamp] = arr[Lamp], arr[i]
                cnt += 1
                if cnt >= Lnum:
                    cnt = 0
                    return arr
            elif Atmp >= Trans(arr):
                arr[Lamp], arr[i] = arr[i], arr[Lamp]
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                cnt += 1
                if cnt >= Lnum:
                    cnt = 0
                    return arr
        return selection_sort2(arr, Lnum)
    elif cnt >= Lnum:
        cnt = 0
        return arr


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = []
    for i in range(len(str(N))):
        arr.append(int(str(N)[i]))
    cnt = 0
    selection_sort2(arr, M)

    print(arr)
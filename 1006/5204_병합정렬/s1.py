import sys
sys.stdin = open("sample_input.txt")

T = int(input())

def merge(arr):
    global count
    if len(arr) < 2:
        return arr

    m = len(arr) // 2

    f_arr = merge(arr[:m])
    b_arr = merge(arr[m:])

    if f_arr[-1] > b_arr[-1]:
        count += 1

    merged = []
    f = b = 0
    while f < len(f_arr) and b < len(b_arr):
        if f_arr[f] < b_arr[b]:
            merged.append(f_arr[f])
            f += 1
        else:
            merged.append(b_arr[b])
            b += 1

    merged += f_arr[f:]
    merged += b_arr[b:]

    return merged



for tc in range(1, 1 + T):
    N = int(input())
    array = list(map(int, input().split()))
    count = 0
    array = merge(array)
    print("#{} {} {}".format(tc, array[N//2] ,count))
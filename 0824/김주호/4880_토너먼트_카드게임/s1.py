import sys
sys.stdin = open("sample_input.txt")


def half(arr, n):
    if len(arr) == 2:
        if arr[0] - arr[1] == -1 or arr[0] - arr[1] == 2:
            return arr[1], n[1]
        else:
            return arr[0], n[0]
    elif len(arr) == 1:
        return arr[0], n[0]
    else:
        m1, n1 = half(arr[:(len(arr) + 1)//2], n[:(len(arr) + 1)//2])
        m2, n2 = half(arr[(len(arr) + 1)//2:], n[(len(arr) + 1)//2:])
        return half([m1, m2], [n1, n2])


for case in range(int(input())):
    N = int(input())
    li = list(map(int, input().split()))
    num = range(N)

    print("#{} {}".format(case + 1, half(li, num)[1] + 1))

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    list_a = list(map(int, input().split()))

    for i in range(len(list_a)-1, 0, -1):
        for j in range(0, i):
            if list_a[j] > list_a[j+1]:
                list_a[j], list_a[j+1] = list_a[j+1], list_a[j]

    a = " ".join(list(map(str, list_a)))
    print('#{} {}'.format(tc, a))
import sys
sys.stdin = open('input.txt')

def in_order(n):
    if int(n):
        in_order(left[int(n)])
        print(list_a[int(n)], end='')
        in_order(right[int(n)])

for tc in range(1, 11):
    print('#{} '.format(tc), end='')
    N = int(input())
    left = [0]*(N+1)
    right = [0]*(N+1)
    list_a = [0]*(N+1)
    for i in range(1, N+1):
        a = list(input().split())
        list_a[i] = a[1]
        if len(a) >= 3:
            left[i] = a[2]
        if len(a) == 4:
            right[i] = a[3]

    in_order(1)
    print()
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    P, A, B = list(map(int, input().split()))

    start = 0
    end = P
    count = 1
    while start <= end:
        middle = (start + end)//2
        if middle == A:
            break;
        elif middle > A:
            end = middle
            count += 1
        else:
            start = middle
            count += 1
    A_count = count

    start = 0
    end = P
    count = 1
    while start <= end:
        middle = (start + end)//2
        if middle == B:
            break;
        elif middle > B:
            end = middle
            count += 1
        else:
            start = middle
            count += 1
    B_count = count

    if A_count < B_count:
        result = 'A'
    elif A_count > B_count:
        result = 'B'
    else:
        result = 0

    print('#{} {}'.format(tc, result))

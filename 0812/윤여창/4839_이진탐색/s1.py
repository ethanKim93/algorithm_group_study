import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    P,A,B = map(int, input().split())
    start = 1
    end = P
    cunt_A, cunt_B = 0, 0


    while True:
        mid = (start + end) // 2
        cunt_A += 1
        if mid == A:
            break
        elif mid < A:
            start = mid
        else:
            end = mid



    start = 1
    end = P
    while True:
        mid = (start + end) // 2
        cunt_B += 1
        if mid == B:
            break
        elif mid < B:
            start = mid
        else:
            end = mid

    result = ''
    if cunt_A < cunt_B:
        result = 'A'
    elif cunt_A > cunt_B:
        result = 'B'
    else:
        result = '0'

    print("#{} {}".format(tc, result))
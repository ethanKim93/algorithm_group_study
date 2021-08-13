import sys
sys.stdin = open('sample_input.txt')

def book_binary_search(P, ans):
    start = 1
    end = P
    cnt = 0

    while start <= end:
        mid = (start + end) // 2
        cnt += 1
        if mid == ans:
            return cnt
        elif mid > ans:
            end = mid
        else:
            start = mid


T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    a_number = book_binary_search(P, A)
    b_number = book_binary_search(P, B)

    if  a_number < b_number:
        result = 'A'
    elif a_number > b_number:
        result = 'B'
    else:
        result = 0

    print('#{} {}'.format(tc, result))
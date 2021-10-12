import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    cnt = 0

    for a in A:
        start = 0
        end = N - 1

        flag = 0
        while start <= end:
            mid = (start + end) // 2

            if a >= A[mid]:
                cnt += 1
                break

                start = mid + 1
                if flag == 1:
                    break
                flag = 1

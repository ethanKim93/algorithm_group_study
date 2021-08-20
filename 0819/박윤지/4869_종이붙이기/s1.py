import sys
sys.stdin = open('sample_input.txt')

T = int(input())
arr = [0] * 31
arr[0] = 1
arr[1] = 1
for i in range(2, 31):
    arr[i] = arr[i - 1] + 2 * arr[i - 2]

for tc in range(1, T+1):
    N = int(input()) // 10
    print('#{} {}'.format(tc, arr[N]))



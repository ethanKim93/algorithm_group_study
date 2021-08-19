import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for test in range(T):

    N = int(input())

    arr = [1, 3] + [0] * (N//10 - 2)    # 배열 생성

    for n in range(2, N//10):
        arr[n] = 2*arr[n-2] + arr[n-1]  # a_n = a_(n-2) *2 + a_(n-1)

    result = arr[N//10 - 1]             # (n-1) index 확인

    print('#{} {}'.format(test+1, result))
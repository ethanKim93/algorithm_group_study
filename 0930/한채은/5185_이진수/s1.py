import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, num = input().split()
    # 16진수니까 *4
    N = int(N)*4
    # int로 1차 10진수로 변환 후 bin으로 2진수로 변환, 앞에 0b가 있으니까 [2:]
    # zfill로 앞에 0으로 자리수 채워주기
    ans = bin(int(num, 16))[2:].zfill(N)
    print('#{} {}'.format(tc, ans))

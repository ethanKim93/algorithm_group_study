# 수경님 코드
import sys
sys.stdin = open('sample_input.txt')

# 10진수 -> 2진수 변환
def num_bit(num):
    global output
    for j in range(3, -1, -1):
        if num & (1 << j):
            output.append('1')
        else:
            output.append('0')


T = int(input())
for tc in range(1, T + 1):
    N, num16 = input().split()
    output = []
    for n in range(int(N)):
        num_bit(int(num16[n], 16))  # 16진수->10진수로 변환하여

    print('#{} {}'.format(tc, ''.join(output)))
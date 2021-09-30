import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, S = input().split()              # 자리수 N, N자리 16진수
    print('#{}'.format(tc), end=' ')

    for i in range(int(N)):
        t = int(S[i], 16)               # 16진수 문자를 10진수로 바꿈 (int의 기능)
        for j in range(3, -1, -1):      # 3번 비트부터 0번 비트까지
            if t & (2 ** j):            # j번 비트가 1인값과 비트 검사
                print(1, end='')
            else:
                print(0, end='')
    print()
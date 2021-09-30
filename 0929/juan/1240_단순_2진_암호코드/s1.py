# 0 ~ 9까지의 수와 대응하는 이진 코드
P = {'0001101': 0,
     '0011001': 1,
     '0010011': 2,
     '0111101': 3,
     '0100011': 4,
     '0110001': 5,
     '0101111': 6,
     '0111011': 7,
     '0110111': 8,
     '0001011': 9}

import sys
sys.stdin = open('input.txt')


def scanner():
    for i in range(N):
        # 끝에서부터(마지막은 1로 고정이니 M-1번부터) 0번째까지
        for j in range(M - 1, -1, -1):
            # 0이면 넘어가고
            if arr[i][j] == '0': continue

            # 1이면 대응하는 숫자를 담을 리스트 준비
            pwd = []

            # 7개 영역에서
            for pos in range(j - 55, j+1, 7):
                # i번 row의 pos~pos+7(-1) 범위의 col에 대응하는 이진코드를 찾아 대응하는 숫자를 넣자
                pwd.append(P[arr[i][pos:pos + 7]])

            # 홀수 & 짝수 자리 합
            odd_digit_sum = pwd[0] + pwd[2] + pwd[4] + pwd[6]
            even_digit_sum = pwd[1] + pwd[3] + pwd[5] + pwd[7]

            # 올바른 검증 코드 -> ((홀수 자리 합) * 3 + 짝수 자리 합) % 10 == 0 -> 10의 배수
            if ((odd_digit_sum * 3 + even_digit_sum) % 10) == 0:
                return odd_digit_sum + even_digit_sum
            # 검증코드가 틀린 경우 0 return
            else:
                return 0


T = int(input())
for tc in range(1, T + 1):
    # N: 세로, M: 가로
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    print('#{} {}'.format(tc, scanner()))
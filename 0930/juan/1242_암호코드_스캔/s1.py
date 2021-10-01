import sys
sys.stdin = open('sample_input.txt')


# 암호 코드 (앞 쪽 0은 무시)
# 참고 -> dict의 key는 mutable 불가능
P = {(2, 1, 1): 0,
     (2, 2, 1): 1,
     (1, 2, 2): 2,
     (4, 1, 1): 3,
     (1, 3, 2): 4,
     (2, 3, 1): 5,
     (1, 1, 4): 6,
     (3, 1, 2): 7,
     (2, 1, 3): 8,
     (1, 1, 2): 9}

# 암호 코드 정보 확인 (16진수 -> 2진수)
hex_to_bin = {'0': [0, 0, 0, 0],
              '1': [0, 0, 0, 1],
              '2': [0, 0, 1, 0],
              '3': [0, 0, 1, 1],
              '4': [0, 1, 0, 0],
              '5': [0, 1, 0, 1],
              '6': [0, 1, 1, 0],
              '7': [0, 1, 1, 1],
              '8': [1, 0, 0, 0],
              '9': [1, 0, 0, 1],
              'A': [1, 0, 1, 0],
              'B': [1, 0, 1, 1],
              'C': [1, 1, 0, 0],
              'D': [1, 1, 0, 1],
              'E': [1, 1, 1, 0],
              'F': [1, 1, 1, 1]}


def scanner():                                      # 2진수 -> 암호코드 변환
    ans = 0
    for i in range(N):                              # 하나의 row씩 체크하며
        j = M*4-1                                   # 인덱스 에러 방지를 위해 -1 (마지막 제외)
        while j >= 55:                              # 최소 가로 길이(56 -> 마지막 55)
            if arr[i][j] and arr[i-1][j] == 0:      # 현재가 1이고 이전이 0 (연속된 1의 개수를 count하기 위함)
                pwd = []
                for _ in range(8):                  # 모든 암호코드는 8개의 숫자로 구성 -> 체크
                    c2 = c3 = c4 = 0                # 암호 코드는 오른쪽 3개의 숫자만 봐도 됨

                    while arr[i][j] == 0:           # 0이면 -> 하나 앞으로
                        j -= 1
                    while arr[i][j] == 1:           # 1이면 -> 하나 앞으로 & c4(1개수) count += 1
                        c4, j = c4+1, j-1
                    while arr[i][j] == 0:           # 0이면 -> 하나 앞으로 & c3(0개수) count += 1
                        c3, j = c3+1, j-1
                    while arr[i][j] == 1:           # 1이면 -> 하나 앞으로 & c2(1개수) count += 1
                        c2, j = c2+1, j-1

                    MIN = min(c2, c3, c4)           # 암호문의 길이가 정해지지 않았기 때문에 최솟값으로 나눠야 한다
                    pwd.append(P[(c2 // MIN, c3 // MIN, c4 // MIN)])

                # 짝수 & 홀수 자리 합
                even_digit_sum = pwd[0] + pwd[2] + pwd[4] + pwd[6]
                odd_digit_sum = pwd[1] + pwd[3] + pwd[5] + pwd[7]

                if (odd_digit_sum * 3 + even_digit_sum) % 10 == 0:
                    ans += odd_digit_sum + even_digit_sum

            j -= 1                                  # 한 칸 앞으로
    return ans


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[] for _ in range(N)]

    for i in range(N):
        tmp = input()
        for j in range(M):
            arr[i] += hex_to_bin[tmp[j]]                # 16진수 -> 2진수 변환 후 배열 입력

    print('#{} {}'.format(tc, scanner()))
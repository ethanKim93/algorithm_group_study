import sys
sys.stdin = open('input.txt')

code = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']


def get_barcode(r):
    for j in range(M-1, -1, -1):
        if arr[r][j] == '1' and (j - 55) >= 0:
            return arr[r][j - 55:j+1]


def decode(bcd):
    li = []
    for k in range(8):
        tmp = bcd[k*7:7+k*7]
        if tmp in code:
            li.append(code.index(tmp))
        else:
            return 0
    return li


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    # 1이 있는 행 찾기
    for i in range(N):
        if '1' in arr[i]:
            # 바코드 부분만 가져와서
            barcode = get_barcode(i)
            # 패스워드로 변환
            password = decode(barcode)
            # 해석 가능한 바코드가 아니라면 다음 행 탐색
            if not password:
                continue

            # 정상적인 암호코드인지 확인
            odd_sum = 0
            even_sum = 0
            confirm = password[7]
            for k in range(7):
                if k % 2:
                    even_sum += password[k]
                else:
                    odd_sum += password[k]
            # 비정상적인 암호코드일 경우 다음 행 탐색
            if (odd_sum * 3 + even_sum + confirm) % 10:
                continue

            print('#{} {}'.format(tc, sum(password)))
            break
    # 정상적인 암호 코드가 없다면 0 출력
    else:
        print('#{} 0'.format(tc))

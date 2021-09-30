import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, num = map(str, input().split())

    num_10 = int(num, 16)
    # 16진수를 10진수로, 0x없어도 인식
    num_2 = format(num_10, 'b')
    # 'b' = 2진수 'o' = 8진수 'x' = 16진수
    while len(num_2) < int(N) * 4:
        # 처음에 if로 했는데 37FE의 경우 15자리가 나오게 되므로 while 로 변경
        # 첫자리가 0인경우는 안보이니 계산해서 붙여주기
        num_2 = '0' + num_2

    print('#{} {}'.format(tc, num_2))


##########################################################################


T = int(input())

# 10 이 넘는 숫자를 위한 변환기
converter = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

for tc in range(1, T+1):
    N, number = input().split()
    # 최종 값 초기화
    result = ''
    # 읽는거는 뒤에서 부터 읽어오자
    for n in number[::-1]:
        # 변환기 안에 있는 숫자라면 변환해주자
        if n in converter:
            n = converter[n]
        # 변환기 안에 없는 숫자는 str로 들어오기 때문에 변환해주기
        n = int(n)
        # 16진수는 무조건 4자리 차지하니 4번 반복해준다.
        for _ in range(4):
            result = str(n % 2) + result
            n //= 2

    print("#{} {}".format(tc, result))


#########################################################################


def b_bit_print(i):
    output = ''
    for j in range(3, -1, -1):                  # 4자리
        output += '1' if i & (1 << j) else '0'  # i의 j자리 비트가 1인지 확인
    return output


T = int(input())
for tc in range(1, T+1):
    N, hex_str = input().split()
    bit_num = ''                                # 2진수로 저장할 변수

    for i in hex_str:
        i = int('0x'+i, 16)                     # 16진수를 10진수로 변경
        bit_num += b_bit_print(i)                # 10진수 하나씩 4비트 2진수로 변경
    print('#{} {}'.format(tc, bit_num))
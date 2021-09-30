import sys
sys.stdin = open('sample_input.txt')

def num_bit(num):
    output = ""
    for j in range(3, -1, -1):
        if num & (1<<j):
            output += '1'
        else:
            output += '0'
    return output

T = int(input())
for tc in range(1, T+1):
    N, num16 = input().split()

    num16_lst = []
    for n in range(int(N)):
        num16_lst.append(num_bit(int(num16[n], 16)))
    ans = ''
    for n in range(int(N)):
        ans += num16_lst[n]
    print('#{} {}'.format(tc, ans))



# 최적화 코드
# str에 붙이는 형태보다 list형태->join 속도가 더 빠름

# 10진수 -> 2진수 변환
def num_bit(num):
    global output
    # for문으로 4자리bit 검사
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
        num_bit(int(num16[n], 16))  # 16진수->10진수로 변환하여 num_bit()실행

    print('#{} {}'.format(tc, ''.join(output)))
import sys
sys.stdin = open('sample_input.txt')


# 10 -> 2진수
def num_bit(num):
    output = ""
    for j in range(3, -1, -1):
        if num & (1<<j):
            output += '1'
        else:
            output += '0'
    return output


# 번호 비율 찾아내기
def find_code(j, flag):
    global hex_binary
    cnt = [0, 0, 0, 0]
    while True:
        if (flag ==4) or (flag == 3 and sum(cnt) % 7 == 0):
            break
        elif hex_binary[j] == hex_binary[j-1]:
            cnt[flag] += 1
            j -= 1
            continue
        else:
            cnt[flag] += 1
            j -= 1
            flag += 1

    multiplied = sum(cnt)//7
    for c in range(4):
        cnt[c] //= multiplied
    tmp = ''.join(map(str, cnt[::-1]))
    amho_num = number.index(tmp)

    return multiplied, amho_num

def isitcode(secret):
    odd = 0
    even = 0
    verify_num = int(secret[-1])
    for i in range(7):
        if i%2 == 0:
            odd += int(secret[i])
        else:
            even += int(secret[i])
    if (odd*3 + even + verify_num)%10 == 0:
        return odd+even+verify_num
    else:
        return 0


T = int(input())-8
for tc in range(1, T+1):
    N, M = map(int, input().split())
    code = [input() for _ in range(N)]
    ans = []
    number = ['3211', '2221', '2122', '1411', '1132', '1231', '1114', '1312', '1213', '3112']

    for i in range(N):
        hex_binary = ''
        if code[i] != '0'*M:
            for j in range(M):
                hex_binary = num_bit(int(code[i][M - 1 - j], 16)) + hex_binary
            m = 0
            while m < len(hex_binary):
                if hex_binary[len(hex_binary) - 1 - m] == '0':
                    m += 1
                else:
                    amho = ''
                    for _ in range(8):
                        multiplied, amho_num = find_code(len(hex_binary) - 1 - m, 0)
                        m += 7*multiplied
                        amho = str(amho_num) + amho

                    ans.append(isitcode(amho))

    if len(ans) != 0:
        print(sum(set(ans)))
    else:
        print(0)



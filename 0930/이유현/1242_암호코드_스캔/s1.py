import sys
sys.stdin = open('sample_input.txt')

pwd_ratio = {'211': 0, '221': 1, '122': 2, '411': 3, '132': 4, '231': 5, '114': 6, '312': 7, '213': 8, '112': 9}


def replace_hex(raw):
    hex_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for h in hex_list:
        raw = raw.replace(h, '{0:b}'.format(int('0x'+h, 16)).zfill(4))
    bin_pwd.append(raw.rstrip('0'))


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 중복되는 라인을 제거한다
    scanner = sorted(list(set([input() for _ in range(N)])))
    # 0으로만 이루어진 배열을 제거한다
    scanner.pop(0)

    bin_pwd = []
    for pwd_line in scanner:
        replace_hex(pwd_line)
    ########################
    #### 2진법으로 변경 ####
    ########################

    # 비율이 늘어난 경우 고려
    pwd_code = []
    total = 0
    for i in range(len(bin_pwd)):
        temp = []
        # 0과 1의 개수를 세어 비율로 비밀번호를 찾는다
        n1 = n2 = n3 = 0
        for j in range(len(bin_pwd[i])-1, -1, -1):
            if bin_pwd[i][j] == '1' and n1 == 0 and n2 == 0:
                n3 += 1
            elif bin_pwd[i][j] == '0' and n1 == 0 and n3 > 0:
                n2 += 1
            elif bin_pwd[i][j] == '1' and n2 > 0 and n3 > 0:
                n1 += 1
            if n1 > 0 and n2 > 0 and n3 > 0 and bin_pwd[i][j] == '0':
                n = min(n1, n2, n3)
                temp.append(pwd_ratio[str(n1//n) + str(n2//n) + str(n3//n)])
                n1 = n2 = n3 = 0
            if len(temp) == 8:
                temp_pwd = temp[::-1]
                if not ((temp_pwd[0] + temp_pwd[2] + temp_pwd[4] + temp_pwd[6]) * 3 + (temp_pwd[1] + temp_pwd[3] + temp_pwd[5]) + temp_pwd[7]) % 10:
                    if temp_pwd not in pwd_code:
                        total += sum(temp_pwd)
                        pwd_code.append(temp_pwd)
                temp = []

    print('#{} {}'.format(tc, total))
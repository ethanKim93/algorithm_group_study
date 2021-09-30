import sys
sys.stdin = open('sample_input.txt')

dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

dict_bit = {'211': '0', '221': '1', '122': '2', '411': '3',
            '132': '4', '231': '5', '114': '6', '312': '7',
            '213': '8', '112': '9'}

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input()[:M] for _ in range(N)]

    two_list = []
    hexa_set = set()
    res = 0
    for r in range(N):
        if arr[r] not in hexa_set:
            bit = ''
            for char in arr[r]:
                bit += dict[char]
            two_list.append(bit)

    key_list = []  # 동일한 암호는 pass
    key = []  # 8개의 숫자를 모으는 리스트
    for two_bit in two_list:
        r1, r2, r3 = 0, 0, 0

        if '1' not in two_bit:
            continue
        for c in range(M * 4 - 1, -1, -1):  # 뒤에서부터 확인
            if r1 == 0 and r2 == 0 and two_bit[c] == '1':  # 맨뒤는 1로 시작한다
                r3 += 1
            elif r3 and r1 == 0 and two_bit[c] == '0':  # 중간 과정은 0
                r2 += 1
            elif r3 and r2 and two_bit[c] == '1':  # 다시 맨 앞쪽은 1
                r1 += 1
            elif r1 and two_bit[c] == '0':
                division = min(r1, r2, r3)
                num = str(r1 // division) + str(r2 // division) + str(r3 // division)
                key.append(int(dict_bit[num]))

                r1 = r2 = r3 = 0
                if len(key) == 8:
                    if key not in key_list:
                        key_list.append(key)
                        if ((key[7] + key[5] + key[3] + key[1]) * 3 + key[6] + key[4] + key[2] + key[0]) % 10 == 0:
                            res += sum(key)
                    key = []

    print('#{} {}'.format(tc, res))







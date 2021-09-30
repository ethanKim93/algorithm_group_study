##못 풀었습니다.

dicct = {  # key: 16진수, value: 2진수
    '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}
code = {'211': 0, '221': 1, '122': 2, '411': 3, '132': 4, '231': 5, '114': 6, '312': 7, '213': 8, '112': 9}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    inp = list(set(input() for _ in range(N)))
    B = []
    for hex in inp:
        if hex.count('0') != M:
            hb = ''
            for h in hex:
                hb += dicct[h]
            B.append(hb.lstrip('0'))

    nums = []
    one = two = three = 0
    for b in B:
        tmp = []
        for i in b:
            if i == '1':
                if two:
                    three += 1
                else:
                    one += 1
            else:
                if one and not three:
                    two += 1
                elif three:
                    minCnt = min(one, two, three)
                    one //= minCnt
                    two //= minCnt
                    three //= minCnt
                    deco = str(one) + str(two) + str(three)
                    nums.append(code[deco])
                    one = two = three = 0
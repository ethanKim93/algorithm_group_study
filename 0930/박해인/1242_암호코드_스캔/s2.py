import sys
sys.stdin = open('sample_input.txt')

h2b = {'0': '0000',       '1': '0001',
       '2': '0010',       '3': '0011',
       '4': '0100',       '5': '0101',
       '6': '0110',       '7': '0111',
       '8': '1000',       '9': '1001',
       'A': '1010',       'B': '1011',
       'C': '1100',       'D': '1101',
       'E': '1110',       'F': '1111'}

pwd = {'211':0, '221':1, '122':2, '411': 3, '132':4, '231':5, '114':6, '312':7, '213':8, '112': 9}

def reduce(c, b, a):
    min_num = min(c,b,a)
    c //= min_num
    b //= min_num
    a //= min_num
    return str(c)+str(b)+str(a)


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())  # N 세로 16 M 가로 26
    arrh = [input() for _ in range(N)]
    arrb = ['']*N

    for i in range(N):
        for j in range(M):
            arrb[i] += h2b[arrh[i][j]]

    result = []
    visited = []
    answer = 0
    for y in range(N):
        c1, c2, c3 = 0, 0, 0
        for x in range(M*4-1, -1, -1):
            if c2 == 0 and c3 == 0 and arrb[y][x] == '1':
                c1 += 1
            elif c1 > 0 and c3 == 0 and arrb[y][x] == '0':
                c2 += 1
            elif c1 > 0 and c2 > 0 and arrb[y][x] == '1':
                c3 += 1

            if c1 > 0 and c2 > 0 and c3 > 0 and arrb[y][x] == '0':
                result.append(pwd[reduce(c3, c2, c1)])
                c1, c2, c3 = 0, 0, 0

            if len(result) == 8:
                result = result[::-1]
                value = (result[0] + result[2] + result[4] + result[6]) * 3 + (result[1] + result[3] + result[5]) + result[7]

                if value % 10 == 0 and result not in visited:
                    answer += sum(result)

                visited.append(result)
                result = []

    print('#{} {}'.format(test_case, answer))
import sys
sys.stdin = open('input.txt')
#####실패
def decrypt():
    startidx = len(li) - 1
    cnt = 7
    for i in range(N):
        for j in range(M-1, -1, -1):
            if li[i][j] == '1':
                code = []
                for k in range(j-55, j, 7):
                    code.append(key[li[i][k:k + 7]])
                a = code[0] + code[2] + code[4] + code[6]
                b = code[1] + code[3] + code[5] + code[7]
                if li[i][j-1] == li[i][j]:
                    for k in range():
                        code.append(key[li[i][k:]])
                    a = code[0] + code[2] + code[4] + code[6]
                    b = code[1] + code[3] + code[5] + code[7]

                if (a * 3 + b) % 10:
                    return 0
                else:
                    return a + b

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    li = [input() for _ in range(N)]
    key = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9,
    }
    key_bi = [
        [3, 2, 1, 1],
        [2, 2, 2, 1],
        [2, 1, 2, 2],
        [1, 4, 1, 1],
        [1, 1, 3, 2],
        [1, 2, 3, 1],
        [1, 1, 1, 4],
        [1, 3, 1, 2],
        [1, 2, 1, 3],
        [3, 1, 1, 2]
    ]
    print('#{} {}'.format(tc, decrypt()))
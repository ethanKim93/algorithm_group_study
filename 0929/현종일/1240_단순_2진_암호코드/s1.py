import sys
sys.stdin = open("input.txt")

pattern = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

for test in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    code = [input() for _ in range(N)]

    temp = ''
    for i in range(N):
        for j in range(M-1, -1, -1):
            if code[i][j] == '1':
                temp = code[i][j-55:j+1]
                break
    result = []
    for i in range(0, len(temp), 7):
        for j in range(10):
            if temp[i:i + 7] == pattern[j]:
                result.append(j)

    valid = (result[0] + result[2] + result[4] + result[6]) * 3 + result[1] + result[3] + result[5] + result[7]

    print('#{} {}'.format(test, sum(result))) if not valid % 10 else print('#{} {}'.format(test, 0))

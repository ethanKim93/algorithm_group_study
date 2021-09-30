import sys
sys.stdin = open('sample_input.txt')
# 0 아닌 부분만 16진수로 변환하면서 끙끙 풀다가 처음부터 전부 2진수로 바꾸고 1트만에 풀었읍니다 감사합니다...
pattern = [[3,2,1,1], [2,2,2,1], [2,1,2,2], [1,4,1,1], [1,1,3,2], [1,2,3,1], [1,1,1,4], [1,3,1,2], [1,2,1,3], [3,1,1,2]]

T = int(input())
for tc in range(1, T+1):
    answer = 0
    code_list = []
    code_number = 0

    N, M = map(int, input().split())
    for _ in range(N):
        num = input()
        result = ''
        empty = 0
        for i in range(M-1, -1, -1):
            n16 = int(num[i], 16)
            for j in range(4):
                result = str(1 & (n16 >> j)) + result

        start = len(result) - 1
        while start > 0:
            maybe_code = ''
            if int(result[start]):
                depth = 1
                remain = 8
                while remain:
                    test = result[start - 7 * depth + 1 : start+1]
                    for p in range(len(pattern)):
                        extend = '0' * pattern[p][0]*depth + '1' * pattern[p][1]*depth  + '0' * pattern[p][2]*depth  + '1' * pattern[p][3]*depth
                        if test == extend:
                            maybe_code = str(p) + maybe_code
                            remain -= 1
                            start -= depth * 7
                            break
                    else:
                        depth += 1
                else:
                    if not maybe_code in code_list:
                        code_list += [maybe_code]

            else:
                start -= 1

    for code_test in code_list:
        tot = 0
        for i in range(8):
            if i%2:
                tot += int(code_test[i])
            else:
                tot += 3 * int(code_test[i])
            # print(tot)
        if not tot%10:
            for j in range(8):
                answer += int(code_test[j])
    print('#{} {}'.format(tc, answer))

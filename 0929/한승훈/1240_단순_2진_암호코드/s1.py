import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    code = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
    N, M = map(int, input().split())
    codes = [input() for i in range(N)]
    queue = ''
    # 코드 추출 단계
    for i in range(N):
        j = M-1
        if '1' in codes[i]:
            while j > 0:
                if codes[i][j] == '1':
                    queue = codes[i][j-55:j+1]
                    break
                else:
                    j -= 1
            break
    ans = []
    for i in range(0,56,7):
        ans.append(code.index(queue[i:i+7]))

    # 검증 단계
    odd = even = 0
    for i in range(0, 7, 2):
        odd += ans[i]
    for j in range(1, 8, 2):
        even += ans[j]
    if (odd*3 + even)%10:
        print('#{} 0'.format(tc))
    else:
        print('#{} {}'.format(tc, sum(ans)))
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = []
    for i in range(5):
        li = list(input())
        li += ['*'] * (15 - len(li))
        arr.append(li)

    result = ''
    # 세로줄 읽기
    for col in range(15):
        for row in range(5):
            if arr[row][col] != '*':
                result += arr[row][col]

    print('#{} {}'.format(tc, result))


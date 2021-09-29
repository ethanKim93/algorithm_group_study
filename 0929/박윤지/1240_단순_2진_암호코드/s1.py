import sys
sys.stdin = open('input.txt', 'r')


# 암호 딕셔너리
password = {'0': '0001101',
            '1': '0011001',
            '2': '0010011',
            '3': '0111101',
            '4': '0100011',
            '5': '0110001',
            '6': '0101111',
            '7': '0111011',
            '8': '0110111',
            '9': '0001011'}

# 위 딕셔너리의 key, value 반대로
password_r = {v:k for k,v in password.items()}


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    # 암호 시작하는 줄 번호 찾기
    row = 0
    for i in range(N):
        if arr[i] != '0' * M:
            row = i
            break

    # 2진수의 뒤에서부터 탐색하여 암호비트패턴이 끝나는 지점 찾기
    end = 0
    for j in range(len(arr[row])-1, -1, -1):
        a = arr[row][j-6:j+1]
        if arr[row][j] == '1' and a in password.values():
            end = j
            break

    # 암호 출력할 리스트
    ans = []

    try:
        while end > 5:
            ans = [password_r[arr[row][end-6:end+1]]] + ans
            end -= 7
    except:
        pass

    ansint = list(map(int, ans))
    total = (ansint[0] + ansint[2] + ansint[4] + ansint[6]) * 3 + (ansint[1] + ansint[3] + ansint[5]) + ansint[7]

    if not total % 10:
        print('#{} {}'.format(tc, sum(ansint)))
    else:
        print('#{} {}'.format(tc, 0))

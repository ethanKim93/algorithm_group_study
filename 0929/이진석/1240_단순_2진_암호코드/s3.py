import sys
sys.stdin = open('input.txt')

decoder = {  # 딕셔너리
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())            # N : 세로(1~49), M : 가로(1~99)
    table = [input() for _ in range(N)]         # 입력 배열
    row = col = 0                               # row : 암호코드가 입력된 첫 행의 번호, col : 암호코드가 입력된 행의 가장 마지막 1의 위치
    for i in range(N):
        for j in range(M-1,-1,-1):              # 각 행의 뒤에서부터 돌면서 처음 1이 등장할 때의 인덱스를 저장
            if table[i][j] == '1':
                row = i
                col = j
                break
        if row:
            break

    code = table[row][col-55:col+1]         # 암호코드 set
    result = 0      # 검증하기위한 변수
    total = 0       # 합

    i = 0
    while i < 56:
        temp = code[i:i+7]                  # 각 자리의 암호코드
        if (i // 7) % 2:                    # 짝수자리 암호 + 검증코드
            result += decoder[temp]         # 해석해서 검증
        else:                               # 홀수자리 암호
            result += decoder[temp] * 3     # 해석해서 검증
        total += decoder[temp]              # 암호코드의 합
        i += 7

    if result % 10:                         # 유효하지 않은 암호코드일때
        answer = 0
    else:                                   # 유효한 코드일 때
        answer = total

    print('#{} {}'.format(tc, answer))
import sys
sys.stdin = open('input.txt')

decoder = {'1101000' : 9, '1110110' : 8, '1101110' : 7, '1111010' : 6, '1000110' : 5 , '1100010' : 4, '1011110' : 3, '1100100' : 2, '1001100' : 1, '1011000' : 0}

def check():                                    # 암호검증
    result = 0                                  # 암호 검증을 위한 변수
    total = 0                                   # 리턴할 변수(코드 합)
    for i in range(8):
        if (i+1)%2:                             # 홀수번째코드 3배 후 더하기
            result += code[i]*3
        else:                                   # 짝수번째 + 검증코드 더하기
            result += code[i]
        total += code[i]

    if result % 10:                             # 1의자리가 0이 아닐경우(올바르지 않은 암호코드) 0 리턴
        return 0

    return total                                # 올바른 암호코드 일경우 코드를 모두 더한 값 리턴

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())            # N : 세로(1~49), M : 가로(1~99)
    table = [input() for _ in range(N)]         # 입력 배열
    row = col = 0                               # row : 암호코드가 입력된 첫 행의 번호, col : 암호코드가 입력된 행의 가장 마지막 1의 위치
    for i in range(N):
        # for j in range(M-56+1):                 # 각 행을 돌면서 56칸이 남을때 까지 1이 등장하지않으면 암호가 없는 행, 1이 등장하면 그 행의 인덱스, 마지막으로등장하는 1의 인덱스를 저장
        #     if table[i][j] == '1':
        #         row = i
        #         for k in range(M-1,-1,-1):      # 뒤에서부터 봤을때 1이 시작하는 지점확인
        #             if table[i][k] == '1':
        #                 col = k
        #                 break
        #         break
        for j in range(M-1,-1,-1):              # 각 행의 뒤에서부터 돌면서 
            if table[i][j] == '1':
                row = i
                col = j
                break
        if row:
            break

    code = []                                   # 암호코드를 저장할 리스트
    for l in range(col,col-56,-7):
        temp = table[row][l:l-7:-1]
        code.insert(0, decoder[temp])
        # if temp == '1101000':       #9
        #     code.insert(0,9)
        # elif temp == '1110110':     #8
        #     code.insert(0,8)
        # elif temp == '1101110':     #7
        #     code.insert(0,7)
        # elif temp == '1111010':     #6
        #     code.insert(0,6)
        # elif temp == '1000110':     #5
        #     code.insert(0,5)
        # elif temp == '1100010':     #4
        #     code.insert(0,4)
        # elif temp == '1011110':     #3
        #     code.insert(0,3)
        # elif temp == '1100100':     #2
        #     code.insert(0,2)
        # elif temp == '1001100':     #1
        #     code.insert(0,1)
        # elif temp == '1011000':     #0
        #     code.insert(0,0)
    print(code)
    # answer = check()
    # print('#{} {}'.format(tc, answer))
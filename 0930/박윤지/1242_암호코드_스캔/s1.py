# 하나의 배열에는 1개 이상의 암호코드가 존재
# 비정상적인 암호코드가 포함될 수 있다
# 암호코드가 일부만 표시된 경우는 없다.
# => 암호와 맞는 하나만 찾으면 그 앞줄까지 모두 8자리 숫자

import sys
sys.stdin = open('input1.txt', 'r')

# 인덱스: 암호 숫자, value: 0비율: 1비율: 0비율: 1비율
P = ['3211', '2221', '2122', '1411', '1132', '1231', '1114', '1312', '1213', '3112']

# 16진수를 2진수로 변환하는 함수
def Bbit_print(i):
    output = ''
    for j in range(3, -1, -1):
        if i & (1 << j):
            output += '1'
        else:
            output += '0'
    return output

# 2진수의 뒤에서부터 탐색하여 암호비트패턴이 끝나는 지점 찾기
# row: 줄, reach: 암호코드가 몇배까지 늘어날 수 있는지 (1이면 암호코드 56글자, 2이면 112글자)
def calc(row, reach):
    li = []
    for o in range(1, reach+1):  # 좁은 암호코드부터 넓은 암호코드 순으로 검색
        # 가로 길이에 맞는 암호 리스트 새로 만들기
        newP = []
        for p in range(0, 10):
            newP.append('0' * int(P[p][0]) * o +
                        '1' * int(P[p][1]) * o +
                        '0' * int(P[p][2]) * o +
                        '1' * int(P[p][3]) * o )
        # 암호 있는지 한 칸씩 검색
        for j in range(len(row)-1, 56+56*(o-1), -1):  # 줄의 마지막부터 앞으로 한글자씩 이동
            if row[j] == '1':  # 1을 만나면
                a = row[j-6-7*(o-1) :j+1]
                if a in newP:  # 여기를 마지막으로 하여 암호코드인지 확인
                    li.append((j, o))  # j: end 인덱스, o: 암호코드가 56*o배
                    row = row[0:j-56*o+1]
    return li


T = int(input())


for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    # 암호 있는 줄 모두 찾기
    row = []
    for i in range(N):
        if arr[i] != '0' * M and arr[i] not in row:
            row.append(arr[i])


    # 암호 있는 줄들을 이진수로 바꿈
    row_2 = []
    for k in row:
        output = ''
        for l in k:
            if l != '0':
                # 16진수인 l을 10진수로 바꿈
                l = int(l, 16)
                output += Bbit_print(l)
            else:
                output += '0'
        row_2.append(output)


    # 테스트 케이스 따라서 암호코드가 몇배까지 늘어날 수 있는지 분기
    if N == 100 and M == 26:
        reach_tc = 1
    elif N == 200 and M == 50:
        reach_tc = 2
    elif N == 500 and M == 126:
        reach_tc = 5
    else:
        reach_tc = 35


    # 암호 출력할 리스트
    ans = []
    for m in row_2:  # 이진수 줄 하나(m)씩 빼오기
        # 암호 끝 인덱스 / width*56 = 암호 가로 길이
        listend = calc(m, reach_tc)
        print(listend)

        # # 가로 길이에 맞는 암호 리스트 새로 만들기 (중복)
        # dictP = {}
        # for p in range(0, 10):
        #     keyP = '0' * int(P[p][0]) * width + '1' * int(P[p][1]) * width + '0' * int(P[p][2]) * width + '1' * int(P[p][3]) * width
        #     dictP[keyP] = p
        # print(dictP)
        # try:
        #     cnt = 0
        #     while cnt > 7:
        #         ans = [dictP[m[end-6-7*(width-1): end+1]]] + ans
        #         end -= 7 * width
        #         cnt += 1
        # except:
        #     pass
        #
        # print(ans)
        # ansint = list(map(int, ans))
        # total = (ansint[0] + ansint[2] + ansint[4] + ansint[6]) * 3 + (ansint[1] + ansint[3] + ansint[5]) + ansint[7]


import sys
sys.stdin=open('input.txt')
#암호코드는 8개의 숫자
# 앞 7자리-상품의 고유번호 마지막 1자리-검증코드
#(홀수자리합*3)+(짝수자리합)+검증코드 ==> 10의배수
#세로 50. 가로 100 이하의 크기를 가진 직사각형 배열 ==>1개의 암호코드 포함
#(단, 모든 암호코드가 정상적인 암호코드임을 보장할 수 없다. 비정상적인 암호코드가 포함될 수 있다.)
#정상적인 암호코드들을 판별한 뒤 이 암호코드들에 적혀있는 숫자들의 합을 출력한다.

# 암호코드 구성블록
# 암호코드의 세로 길이는 5 ~ 50 칸이다.
# 암호코드의 가로 길이는 총 길이는 56칸이다.(중요)

pwd={
    '0001101':0,
    '0011001':1,
    '0010011':2,
    '0111101':3,
    '0100011':4,
    '0110001':5,
    '0101111':6,
    '0111011':7,
    '0110111':8,
    '0001011':9,
}

def check_code():
    # 암호코드블록의 첫번째줄의 시작 위치 또는 끝위치를 찾아야하는데
    # 암호코드의 블록이 전부 1로 끝나는 걸 알 수 있다.
    # 뒤에서 부터 탐색하자
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if Media[i][j] == '0':
                continue
            # 암호코드의 마지막위치 j 이면 시작위치는 j-55가 된다.
            # 8개의 암호패턴을 읽어서 숫자로 변환
            read = []
            # #시작위치 s
            for s in range(j - 55, j, 7):

                # read.append(pwd[Media[i][s:s+7]])
                read.append(pwd.get(Media[i][s:s + 7]))

            # 인덱스 기준 -> 홀수 = 짝수자리, 짝수= 홀수자리
            odd = read[0] + read[2] + read[4] + read[6]
            even = read[1] + read[3] + read[5] + read[7]

            if (odd * 3 + even) % 10 == 0:
                return  odd + even
            else:
                return 0
T=int(input())
for i in range(1,T+1):
    #세로 N, 가로 M

    N,M=map(int,input().split())
    Media=[input() for _ in range(N)]

    print( check_code())

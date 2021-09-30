# 보충
import sys
sys.stdin = open('1242.txt')

def erase(i, j, r):
    cnt = i
    while arrb[cnt][j] == 1:
        cnt += 1
    for r in range(r, cnt):
        for c in range(j-56*ratio+1, j+1):
            arr[r][c] = 0

h2b = {'0': '0000',
       '1': '0001',
       '2': '0010',
       '3': '0011',
       '4': '0100',
       '5': '0101',
       '6': '0110',
       '7': '0111',
       '8': '1000',
       '9': '1001',
       'A': '1010',
       'B': '1011',
       'C': '1100',
       'D': '1101',
       'E': '1110',
       'F': '1111'
       }

pwd = {211:0, 221:1, 122:2, 411: 3, 132:4, 231:5, 114:6, 312:7, 213:8, 112: 9}

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())  # N 세로 16 M 가로 26
    arrh = [input() for _ in range(N)]
    arrb = ['']*N

    for i in range(N):
        for j in range(M):
            for k in range(4):
                arrb[i][j+] += h2b[arrh[i][j]]
            # 16진수 배열을 통채로 2진수 배열로 바꾸기

    # 암호 패턴의 끝 위치 찾기
    M *= 4
    for i in range(N):
        j = M-1
        num = [0]*8
        k = 0  # 찾은 암호 숫자의 갯수
        while j >= 0:
            while j >= 0 and arrb[i][j] == '0':  # 1을 만날 때 까지 이동
                j -= 1
            c1 = 0
            if k == 0:
                col = j
            while j >= 0 and arrb[i][j] == '1':
                c1 += 1
                j -= 1
            c2 = 0
            while j >= 0 and arrb[i][j] == '0':
                c2 += 1
                j -= 1
            c3 = 0
            while j >= 0 and arrb[i][j] == '1':
                c3 += 1
                j -= 1
            # 0은 세지 않아도 c1,c2,c3만 봐도 비율이 다르기 때문게 구분할 수 있다.
            if c1:
                ratio = min(c1, c2, c3)
                num[7-k] = pwd[c3//ratio*100+c2//ratio*10+c1//ratio]
                k += 1
                if k == 8:
                    print(ratio)
                    print(*num)
                    erase(i, col, ratio)
                    print()


# 김민현
import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    #이중 리스트로 만들기
    arr = [input() for _ in range(N)]


    for i in range(N):
        flag1 = True # 가로줄
        flag2 = True # 세로줄
        for j in range(N-M+1):
                for k in range(M//2):
                    if arr[i][j+k] == arr[i][j+M-1-k]:
                        pass
                    else:
                        flag1 = False
                    if arr[j+k][i] == arr[j+M-1-k][i]:
                        pass
                    else:
                        flag2 = False
                if flag1 == True:
                    result = ''
                    for ch in arr[i][j:j+M]:
                        result += ch
                    print('#{} {}'.format(tc,result))
                if flag2 == True:
                    result = ''
                    for c in range(M):
                        result += arr[j+c][i]
                    print('#{} {}'.format(tc,result))

                flag1 = True
                flag2 = True
import sys
sys.stdin = open('input.txt')

def Palindrome(N,arr):
    for n in range(100): # n 행에 회문이 있는지 검사
        for k in range(n+1): # 확인할 영역의 시작 인덱스
            for l in range(N):
                flag = 1 # 이번 영역이 회문이라 가정
                M = N - n
                for g in range(M // 2): # 비교할 왼쪽 원소의 인덱스
                    if arr[l][k+g] != arr[l][k+M-1-g]:
                        flag = 0 # 회문이 아니면
                        break  # 해당 영역 비교 중지
                if flag:
                    return len(arr[l][k:k+M])

for T in range(10):
    tc = int(input())
    N = 100
    arr = [list(input()) for _ in range(100)] # 가로 회문을 찾기위해 리스트로 받음
    arr_T = [['']*100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            arr_T[j][i] =arr[i][j] # 세로 회문을 찾기위해 기존 행렬을 전치 행렬로 만듬


    ans = Palindrome(N,arr)
    ans_T = Palindrome(N,arr_T)
    if ans >= ans_T:
        result = ans
    else:
        result = ans_T       # 가로, 세로 행렬 비교후 큰쪽 출력
    print('#{} {}'.format(tc,result))


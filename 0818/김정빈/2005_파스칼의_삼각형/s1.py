import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pas = [[1]*_ for _ in range(1, N+1)] #결과값 넣을 빈 리스트
    for i in range(1, N-1): #리스트열 1번째부터 끝까지
        for j in range(len(pas[i])-1): #처음-끝 순회
            pas[i+1][j+1] = pas[i][j] + pas[i][j+1] #다음열행칸은 해당칸+해당열전행칸
    print('#{}'.format(tc))
    for p in pas:
        print(*p)

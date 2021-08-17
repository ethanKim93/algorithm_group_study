import sys
sys.stdin = open('sample_input.txt','r',encoding='utf-8' )

T = int(input())
for i in range(1, T+1):
    n,m = map(int,input().split())
    lis1=[]
    result=[]

    for j in range(n):
        lis1.append(input())
        for k in range(n-m+1):         # 20 , 13 일때를 검사하기 위해
            width = lis1[j][k:k + m]   # 가로 문자열
            if width == width[::-1]:   # 회문 검사
                result.append(width)

    lis2=[]
    lis_ch= ''
    for x in range(n):
        for y in lis1:
            lis_ch += y[x]
        lis2.append(lis_ch)
        lis_ch = ''
    #print(lis2)                   # 세로열만 뽑은 문자열

    for words in lis2:
        for words1 in range(n-m+1):
            hight = words[words1:m + words1]
            if hight == hight[::-1]:          # 회문 검사
                result.append(hight)

    print('#{} {}'.format(i,''.join(result)))

















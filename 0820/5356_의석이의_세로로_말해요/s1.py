import  sys
sys.stdin=open('input.txt')
T=int(input())
for tc in range(1,T+1):
    arrlist=[list(input()) for _ in range(5)]
    maxNum=0
    text=[]
    for i in range(5):
        if maxNum<len(arrlist[i]):
            maxNum=len(arrlist[i])

    for i in range(maxNum): #0~6 가로
        for j in range(5): #0~5 세로
            if len(arrlist[j])-1>=i:
                text.append(arrlist[j][i])

    result=''.join(text)
    print('#{} {} '.format(tc,result))
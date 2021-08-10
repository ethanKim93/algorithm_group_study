import sys
sys.stdin=open('input.txt')
T=10
for tc in range(1,T+1):
    DumN=int(input())
    Box=list(map(int,input().split()))

    #배열의 크기만큼 반복문
    for i in range(len(Box)):
        #배열의 총크기에서 i값과 1 뺀만큼 감소하여 비교
        for j in range(0,len(Box)-i-1):
            if Box[j]>Box[j+1]:
                Box[j], Box[j+1]=Box[j+1],Box[j]
    L=0
    R=len(Box)-1
    C=0

    while True:

        if C==DumN:
            break

        if Box[L] >= Box[R]:
            L += 1
            R -= 1

        if Box[L]<=Box[R]:
            Box[L]+=1
            Box[R]-=1
            C += 1


        for i in range(len(Box)):
            # 배열의 총크기에서 i값과 1 뺀만큼 감소하여 비교
            for j in range(0, len(Box) - i - 1):
                if Box[j] > Box[j + 1]:
                    Box[j], Box[j + 1] = Box[j + 1], Box[j]


    result = Box[len(Box) - 1] - Box[0]
    print('#{} {}'.format(tc,result))


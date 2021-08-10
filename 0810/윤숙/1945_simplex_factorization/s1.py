import sys
sys.stdin=open('input.txt')
T=int(input())

for tc in range(1,T+1):
    N=int(input())
    Numbers=[0]*5
    result=''
    while True:
        if N==1:
            break
        if N%2==0:
            N//=2
            Numbers[0]+=1
        if N%3==0:
            N//=3
            Numbers[1]+=1
        if N%5==0:
            N//=5
            Numbers[2]+=1
        if N%7==0:
            N//=7
            Numbers[3]+=1
        if N%11==0:
            N//=11
            Numbers[4]+=1

    for i in Numbers:
        result+=str(i)+'\t'

    print('#{}  {}'.format(tc, result))
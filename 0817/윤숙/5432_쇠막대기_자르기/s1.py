import sys
sys.stdin=open('input.txt')
T=int(input())
for tc in range(1,T+1):
    EX= list(map(str, sys.stdin.readline().split('\n')[0]))
    print(EX)
    arr=[0]*len(EX)
    for i in range(0,len(EX)):
        if EX[i]=='(' and EX[i+1]==')':
            arr[i]=1
            arr[i+1] = 1




    print(arr)
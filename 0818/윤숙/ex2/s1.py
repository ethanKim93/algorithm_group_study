import sys
sys.stdin=open('input.txt')
T=2
for tc in range(1,T+1):
    text=list(input())
    cnt=0
    N=len(text)
    stack=[]
    for i in range(N):
        if text[i]=='(':
            stack.append(text[i])

        if text[i]==')':
            stack.pop(-1)
            cnt+=1


    if stack:
        print(False) # 괄호가 있으면 False
    else : print(True) # 괄호가 없으면 True

    # print(stack) # 괄호를 출력
    # print(cnt) #괄호 쌍의 갯수
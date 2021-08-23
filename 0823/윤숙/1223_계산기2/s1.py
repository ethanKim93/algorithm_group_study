import sys
sys.stdin=open('input.txt')
T=10
def cac(token,a,b):
    if token=='+':
        return a+b
    elif token=='*':
        return a*b


for tc in range(1,T+1):
    N=int(input())
    arr=list(input())

    stack = []
    for num in arr:
        if type(num) is int:
            stack.append(num)

        elif num == '+':
            n1 = arr.pop()
            n2 = arr.pop()
            stack.append(int(n2) + int(n1))

        elif num == '*':
            n1 = arr.pop()
            n2 = arr.pop()
            stack.append(int(n2) * int(n1))

    c=[]
    for token in stack:
        if token in '1234567890':
            c.append(int(token))

        elif token in '+*':
            a=c.pop()
            b=c.pop()
            result= cac(token, b,a)
            c.append(result)

    total=c.pop()



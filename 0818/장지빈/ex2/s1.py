import sys
sys.stdin = open('input.txt')

def stack_push(n):
    global ls
    ls.append(n)

def stack_pop():
    global ls
    if len(ls)==0:
        return False
    else:
        return ls.pop()

T = int(input())
for tc in range(1, T+1):
    ls = []
    checkls = list(input())
    for i in checkls:
        if i == '(':
            stack_push('(')
        else:
            stack_pop()
    if ls == []:
        print(True)
    else:
        print(False)
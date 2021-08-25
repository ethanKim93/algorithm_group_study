import sys
sys.stdin = open('input.txt')

# 후위표기법으로 변경
def change(eq):
    Stack = []
    Count = []
    for i in range(len(eq)):
        # 숫자일 때 그냥 append
        if eq[i].isdigit():
            Count.append(eq[i])
            continue
        # 괄호가 있는지 체크하고 추가
        if eq[i] == '(':
            Stack.append(eq[i])
            continue
        # 더하기 일때
        elif eq[i] == '+':
            while Stack:
                if Stack[-1] == '(': break
                Count.append(Stack.pop())
            Stack.append(eq[i])
            continue
        # 곱하기 일때
        elif eq[i] =='*':
            while Stack[-1] =='*':
                Count.append(Stack.pop())
            Stack.append(eq[i])
            continue
        elif eq[i] == ')':
            while Stack:
                if Stack[-1] == '(':
                    Stack.pop()
                    break
                Count.append(Stack.pop())
    return Count

T = 10

for tc in range(1, T+1):
    N =int(input())
    lst = list(input())

    s1 = change(lst)
    s2 = []

    for j in s1:
        if j == '+':
            temp1 = s2.pop()
            temp2 = s2.pop()
            s2.append(temp1+temp2)
        elif j == '*':
            temp1 = s2.pop()
            temp2 = s2.pop()
            s2.append(temp1*temp2)
        else:
            s2.append(int(j))
    print('#{} {}'.format(tc,s2[0]))

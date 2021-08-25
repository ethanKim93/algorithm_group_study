import sys
sys.stdin = open('input.txt')

T = 10
icp = {'*': 2, '+': 1, '(': 0}

def postfix(text, stack):
    for i in text:
        if i in list(map(str, range(0, 10))):
            result.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            is_close(i, stack)
        else:
            cal_icp(i, stack)
    for _ in stack:
        result.append(stack.pop())
    return result


def cal_icp(i, stack):
    if not stack:
        stack.append(i)
        return
    if icp[i] > icp[stack[-1]]:  # 부등호 > 맞음
        stack.append(i)
    else:
        result.append(stack.pop())
        cal_icp(i, stack)


def is_close(i, stack):
    if not stack:
        stack.append(i)
        return
    else:
        if stack[-1] != '(':
            result.append(stack.pop())
            is_close(i, stack)
        else:
            stack.pop()


for tc in range(1, T+1):
    length = int(input())
    text = input()
    stack = []  # 연산자가 잠깐 머무는 스택
    result = []  # 완성된 후위식 담김
    postfix(text, stack)
    for s in stack:  # 스택에서 남은 거 후위식에 넣어줘야함
        result.append(s)

    stackCal = []  # 계산된 답 담김
    for j in result:
        if j in list(map(str, range(0, 10))):
            stackCal.append(j)
        else:
            b = int(stackCal.pop())
            a = int(stackCal.pop())
            if j == '*':
                stackCal.append(a*b)
            elif j == '+':
                stackCal.append(a+b)


    print('#{} {}'.format(tc, stackCal.pop()))

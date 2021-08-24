import sys
sys.stdin = open('input.txt')


def backdata(data):
    back_str = ''

    for i in data:
        if '0' <= i <= '9':
            back_str += i
            continue
        elif i == '(':
            stack.append(i)
        elif i == '+':
            while stack:
                if stack[-1] == '(': break
                back_str +=(stack.pop())
            stack.append(i)
            continue
        elif i == '*':
            while stack[-1] == '*':
                back_str += (stack.pop())
            stack.append(i)
            continue
        elif i == ')':
            while 1:
                if stack[-1] == '(':
                    stack.pop()
                    break
                else:
                    back_str += stack.pop()
    return back_str

def cal(data):
    cal_stack = []
    for i in data:
        if '0' <= i <= '9':
            cal_stack.append(int(i))
        elif len(cal_stack) >= 2:
            a = cal_stack.pop()
            b = cal_stack.pop()
            if i == '+':
                cal_stack.append(b + a)
            elif i == '*':
                cal_stack.append(b * a)
    return cal_stack



for tc in range(1,11):
    N = int(input())
    data = list(input())
    stack = []
    back_data = []
    print('#{} {}'.format(tc,*cal(backdata(data))))



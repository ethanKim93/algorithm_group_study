import sys
sys.stdin = open('input.txt')


def push(item):
    stack.append(item)


def pop():
    return stack.pop()


def peek():
    return stack[-1]


def priority(a):
    global changed_formula

    priority = {'+': 1, '*': 2}
    if priority[a] > priority[peek()]:  # 우선순위가 높으면
        push(a)
    else:  # 우선순위가 낮으면
        while stack and priority[a] <= priority[peek()]:
            changed_formula += pop()
        push(a)

def calculate(formula):  #후위표현식 연산
    result = []   # 기존 stack 쓰면 안될 거 같아서 새로 만들어줬는데 그냥 stack써도 될 거 같기도 하고,,
    # 1. 피연산자를 만나면 stack에 push
    for a in formula:
        if a in numbers:
            result.append(int(a))
        elif a == '+':          # 2. 연산자를 만나면 필요한만큼의 피연산자를 stack에서 pop하여 연산하고, 다시 stack에 push 한다.
            num = result.pop()
            result[-1] += num
        else:
            num = result.pop()
            result[-1] *= num

    return result[0]


for test_case in range(1, 11):
    N = int(input())  # 테스트케이스의 길이
    formula = list(input())
    stack = []
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    changed_formula = ''

    for a in formula:
        if a in numbers:  # a가 피연산자라면
            changed_formula += a
        else:  # 연산자라면
            if not stack:  # 비어있다면
                push(a)
            else:
                if a == '*' and peek() == '+':
                    push(a)
                else:
                    priority(a)

    # 스택에 남은 것 비우기
    for i in range(len(stack)):
        changed_formula += pop()

    # 후위표현식 계산하기
    answer = calculate(changed_formula)

    print('#{} {}'.format(test_case, answer))
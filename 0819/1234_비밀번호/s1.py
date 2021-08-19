import sys
sys.stdin = open('input.txt')


def push(item):
    stack.append(item)


def pop():
    return stack.pop()


def make_password(s):

    for number in s:
        if stack:
            if stack[-1] == number:
                pop()  # 중복문자 제거
            else:  # 중복이 아닌 문자는 stack에 추가
                push(number)
        else:  # 스택이 비어있다면, stack에 추가
            push(number)

    return stack

for test_case in range(1, 11):
    N, numbers = input().split()  # 문자열의 길이 N
    numbers = list(numbers)

    stack = []

    password = "".join(make_password(numbers))
    print('#{} {}'.format(test_case, password))

import sys
<<<<<<< HEAD
sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t + 1):
    temps = []
    ans = 1
    text = list(input())
    for i in text:
        if i == "(":
            temps.append(i)
        elif i == ")":
            if not temps: # 뺄 값이 없을 경우
                ans = 0
                break

            elif temps.pop() != "(": # 뺀 값이 '('이 아닐 경우
                ans = 0
                break
        elif i == "{":
            temps.append(i)
        elif i == "}":
            if not temps: # 뺄 값이 없을 경우
                ans = 0
                break

            elif temps.pop() != "{": # 뺸 값이 '{'이 아닐 경우
                ans = 0
                break


    if temps:
        ans = 0

    print("#{} {}".format(tc, ans))
=======
sys.stdin = open('sample_input.txt')


def push(item):
    stack.append(item)


def pop():
    if stack:
        return stack.pop()


def check(text):
    for i in range(len(text)):
        if text[i] == '(' or text[i] == '{':
            push(text[i])

        elif text[i] == ')':
            if stack and stack[-1] == '(':
                pop()
            else:
                return 0

        elif text[i] == '}':
            if stack and stack[-1] == '{':
                pop()
            else:
                return 0
    if stack:
        return 0
    else:
        return 1


T = int(input())
for test_case in range(1, T+1):
    code = input()
    stack = []
    print('#{} {}'.format(test_case, check(code)))


>>>>>>> 92ff47ec2ac89df817400374cabd441bfa841964

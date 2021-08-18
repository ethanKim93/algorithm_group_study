import sys
sys.stdin = open('input.txt')

def push(item):
    global test_list
    test_list.append(item)


def pop():
    global test_list

    if len(test_list) == 0:
        return
    else:
        return test_list.pop(-1)


for tc in range(1, 7):
    bracket = input()
    test_list = []

    for i in range(len(bracket)):
        if bracket[i] == '(' or bracket[i] == '{' or bracket[i] == '[':
            push(bracket[i])
        elif bracket[i] == ')':
            if len(test_list) == 0 or pop() != '(':
                print('error')
                break
        elif bracket[i] == '}':
            if len(test_list) == 0 or pop() != '{':
                print('error')
                break
        elif bracket[i] == ']':
            if len(test_list) == 0 or pop() != '[':
                print('error')
                break
        if len(bracket)-1 == i:
            if len(test_list):
                print('error')
            else:
                print('ok')


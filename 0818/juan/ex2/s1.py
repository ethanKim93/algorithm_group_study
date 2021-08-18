import sys
sys.stdin = open('input.txt')

stack = []

def push(item):
    stack.append(item)

def pop():
    if stack:
        return stack.pop()

def check(data):
    for i in range(len(data)):
        if data[i] == '(':          # 여는 괄호인 경우 stack에 추가
            push(data[i])

        else:                       # 닫는 괄호인데
            if stack:               # stack이 채워져있으면
                pop()               # stack 마지막 항목 꺼냄
            else:                   # stack이 비었으면
                return False        # 짝이 맞지 않으니 False 반환

    if stack:                       # 반복이 끝났을때 stack이 채워져있으면
        return False                # 짝이 맞지 않으니 False 반환
    else:                           # 반복이 끝났을때 stack도 비었으면
        return True                 # 짝이 맞았으니 True 반환

for i in range(2):
    data = input()
    print(check(data))
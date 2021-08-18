# ex2 - 괄호 검사
import sys
sys.stdin = open('input.txt')


class Stack:
    # 리스트를 이용하여 스택 생성
    def __init__(self):
        self.stack = []

    # PUSH
    def push(self, item):
        self.stack.append(item)

    # POP
    def pop(self):
        if self.isEmpty():
            return
        else:
            return self.stack.pop()

    # 스택에서 top의 값 읽어오기
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return None

    # 스택이 비어있는지 확인
    def isEmpty(self):
        return len(self.stack) == 0


# 괄호 검사
def check(p):
    for char in p:
        if char == '(':
            s.push(char)
        elif char == ')':
            if not s.isEmpty():
                s.pop()
            else:
                return False
    if not s.isEmpty():
        return False
    else:
        return True


for _ in range(2):
    s = Stack()
    p = input()

    for char in p:
        if char == '(':
            s.push(char)
        elif char == ')':
            if not s.isEmpty():
                s.pop()
            else:
                print(False)
                break
    else:
        if not s.isEmpty():
            print(False)
        else:
            print(True)

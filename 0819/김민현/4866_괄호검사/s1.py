import sys
sys.stdin = open("sample_input.txt")

class Stack:
    def __init__(self):
        self.data = []

    def check(self):
        if len(self.data) == 0:
            return 0
        else:
            return 1

    def push(self,item):
        self.data.append(item)

    def pop(self,item):
        if self.check() != 0:
            self.data.pop(-1)
        else:
            return -1
    def last_data(self):
        return self.data[-1]

    def __str__(self):
        return str(self.data)


for tc in range(1,int(input())+1):
    stack1 = Stack()
    check_str = input()
    result = 0
    for ch in check_str:
        if ch == '{' or ch == '(':
            stack1.push(ch)

        if ch == '}':
            if stack1.check() != 0 and stack1.last_data() == '{':
                stack1.pop(ch)
            else:
                break
        elif ch == ')':
            if stack1.check() != 0 and stack1.last_data() =='(':
                stack1.pop(ch)
            else:
                break
    else:
        if stack1.check() == 0:
            result = 1

    print('#{} {}'.format(tc,result))
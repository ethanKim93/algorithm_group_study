import sys
sys.stdin = open("sample_input.txt")

def calc():
    for i in eqn:
        if i.isdecimal():
            stack.append(int(i))
        elif i == '*':
            try: stack.append(int(stack.pop()) * int(stack.pop()))
            except: return 'error'
        elif i == '/':
            d = int(stack.pop())
            n = int(stack.pop())
            try: stack.append(n//d)
            except: return 'error'
        elif i == '+':
            try: stack.append(int(stack.pop()) + int(stack.pop()))
            except: return 'error'
        elif i == '-':
            try: stack.append(-1*(int(stack.pop()) - int(stack.pop())))
            except: return 'error'
        elif i == '.':
            if len(stack) == 1:
                return stack.pop()
            else: return 'error'
        else:
            return 'error'

for tc in range(1, int(input())+1):
    eqn = input().split()
    stack = []
    print('#{} {}'.format(tc, calc()))


import sys
sys.stdin = open('sample_input.txt')

def push(stack, item):
    stack.append(item)

def pop(stack):
    return stack.pop(-1)

def test(stack, arr):
    for br in arr:
        if br in ['(', '{']:
            push(stack, br)
        elif br in [')', '}']:
            try:
                ends = pop(stack)
                if (br == ')' and ends == '(') or (br == '}' and ends == '{'):
                    pass
                else:
                    return 0
            except:
                return 0
    if stack:
        return 0
    else:
        return 1

T = int(input())

for tc in range(1, T+1):
    string = input()
    stack = []
    print('#{} {}'.format(tc, test(stack, string)))






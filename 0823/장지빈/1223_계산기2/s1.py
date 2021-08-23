import sys
sys.stdin = open('input.txt')

def cal(text):
    stack = []  # *+
    sub = []    # num
    subsum = 0
    for i in text:
        if i == '*' or i == '+':
            stack.append(i)
        else:
            sub.append(i)
    while stack:
        stackpop = stack.pop()
        if stackpop == '*':
            sub.append(int(sub.pop()) * int(sub.pop()))
        else:
            subsum += int(sub.pop())
    return int(sub.pop()) + subsum

for tc in range(1, 11):
    tcl = int(input())
    text = input()
    stack = sub = []
    print('#{} {}'.format(tc, cal(text)))
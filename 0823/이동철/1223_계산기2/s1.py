import sys
sys.stdin = open('input.txt')


# 우선순위
def priority(char):
    if char == '*':
        return 3
    if char == '+':
        return 2
    else:
        return 1


# 중위 -> 후위
def make_postfix():
    stack = []
    processed = []
    for i in range(N):
        num = priority(formula[i])
        # stack 안의 값과 formula값 비교하며 우선순위 판단 후 우선순위 낮은 거 나올때까지 pop
        if num == 3:
            while stack:
                if priority(stack[-1]) < num:
                    break
                processed.append(stack.pop())
            stack.append(formula[i])
        elif num == 2:
            while stack:
                if priority(stack[-1]) < num:
                    break
                processed.append(stack.pop())
            stack.append(formula[i])
        else:
            processed.append(int(formula[i]))

    # 다 돌고나서 스택에 남아 있는 거 추가
    while stack:
        processed.append(stack.pop())
    return processed


# 후위표기 - > 계산
def calculate(arr):
    stack = []
    for i in range(N):
        if arr[i] == '+':
            B = stack.pop()
            A = stack.pop()
            stack.append(A + B)
        elif arr[i] == '*':
            B = stack.pop()
            A = stack.pop()
            stack.append(A * B)
        else:
            stack.append(arr[i])
    return stack


T = 10
for tc in range(1, 11):
    N = int(input())
    formula = input()
    print('#{} {}'.format(tc, *calculate(make_postfix())))

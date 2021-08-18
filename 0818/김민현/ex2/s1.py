import  sys
sys.stdin = open('input.txt')

for _ in range(2):
    arr = input()

    stack = []
    result = True
    for i in range(len(arr)):
        k = stack
        if len(stack) == 0: # stack에 아무것도 없는 경우
            if arr[i] == ')':
                result = False
            else:
                stack.append(arr[i])
        elif arr[i] == ')': # 닫는 괄호가 나왔을 경우
             if stack[-1] == '(':
                stack.pop(-1)
             else:
                 result = False
        else: # 그외 (여는 괄호가 나올때)
            stack.append(arr[i])
    if len(stack) != 0:
        result = False
    print(result)


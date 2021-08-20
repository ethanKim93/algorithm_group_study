import sys
sys.stdin = open("input.txt")

for tc in range(1,11):
    num,input_str = input().split()
    stack = []
    for i in range(len(input_str)):
        if len(stack) != 0 :
            if stack[-1] == input_str[i]:
                stack.pop(-1)
            else:
                stack.append(input_str[i])
        else:
            stack.append(input_str[i])
    print('#{} {}'.format(tc,''.join(stack)))

# a = '2+3*4/5'
# b = list(a)
# stack = []
#
# for i in b:
#     if '0' <= i <= '9':
#         print(i, end='')
#     else:
#         stack.append(i)
#
# print(stack.pop(), end='')
# print(stack.pop(), end='')
# print(stack.pop(), end='')
##############################
#step2.
c = '6528-*2/+'
stack = []
for i in c:
    if '0' <= i <= '9':
        stack.append(int(i))
    else:
        a = stack.pop()
        b = stack.pop()
        if i == '+':
            stack.append(b + a)
        elif i == '-':
            stack.append(b - a)
        elif i == '/':
            stack.append(b / a)
        else:
            stack.append(b * a)

print(stack)
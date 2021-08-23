def push(n):
    stack.append(n)

stack = []
oper = ['+', '_', '/', '*']
arr = list('2+3*4/5')

for a in arr:
    if a in oper:
        push(a)
    else:
        print(a, end=" ")

for _ in range(len(stack)):
    print(stack.pop(), end=" ")
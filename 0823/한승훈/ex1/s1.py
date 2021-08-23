re = input()
four = ['+', '-', '*', '/']
stack = []
for num in re:
    if num in four:
        stack.append(num)
    else:
        print(num, end='')
print(''.join(stack[::-1]))

def postfix(text):
    stack = []
    for i in text:
        if i in map(str, range(0, 10)):
            print(i, end='')
        elif i == ' ':
            pass
        else:
            stack.append(i)
    while stack:
        elem = stack.pop()
        print(elem, end='')


postfix('2 + 3 * 4 / 5')
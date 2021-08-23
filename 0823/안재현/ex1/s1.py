a = input()
stack = []
res = ''
res2 = ''
for x in a:
    if x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9' or x == '0':
        res += x
    else:
        if x == '*' or x == '/' or x == '+' or x == '-':
            while stack:
                res2 += stack.pop()
        stack.append(x)
while stack:
    res2 += stack.pop()
print(res+res2[::-1])

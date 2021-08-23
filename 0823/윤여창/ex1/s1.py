strr = '2+3*4/5'
operator = ['+', '*', '/', '-']
stack = []
#2345/*+ 출력형태

for i in strr:
    if i in operator:
        stack.append(i)
    else:
        print(i, end='')

while len(stack):
    print(stack.pop(), end='')
my_string = input()
stack = []

for i in range(len(my_string)):
    if my_string[i] == '+' or my_string[i] == '-' or my_string[i] == '*' or my_string[i] == '/':        # 연산자가 나오면 
        stack.append(my_string[i])                                                                      # stack에 넣고
    else:                                                                                               # 피연산자가 나오면
        print(my_string[i], end='')                                                                     # 출력하자

while stack:                        # stack이 빌때까지 꺼내면서 출력
    print(stack.pop(), end='')
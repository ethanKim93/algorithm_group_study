s = [0, 0, 0]
top = -1


def push(n):
    global top
    top += 1
    s[top] = n


def pop():
    global top
    s[top] = 0
    # return s[top+1]
    top -= 1


push(1)
push(2)
push(3)
pop()
pop()
pop()
print(s)


# stack_list = list()
#
# def push(data):
#     stack_list.append(data)
#
# def pop():
#     data = stack_list[-1]
#     del stack_list[-1]
#     return data
#
# for index in range(10):
#     push(index)
#
# print(stack_list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# pop()  # 9
# print(stack_list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8]

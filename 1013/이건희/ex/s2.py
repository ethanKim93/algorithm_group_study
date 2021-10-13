def stack(li):
    stack_list = [0]*3
    start = -1
    top = -1
    # Push
    for i in range(len(li)):
        top += 1
        stack_list[top] = li[i]

    print(*stack_list)

    # Pop
    for i in range(len(li)):
        start += 1
        print(stack_list[start],end=" ")

stack([1,2,3])
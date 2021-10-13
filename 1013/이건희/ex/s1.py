def stack(li):
    stack_list = [0]*3
    top = -1
    # Push
    for i in range(len(li)):
        top += 1
        stack_list[top] = li[i]

    print(*stack_list)

    # Pop
    for i in range(len(li)):
        print(stack_list[top],end=" ")
        top -= 1

stack([1,2,3])
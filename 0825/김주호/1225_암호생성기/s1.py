for _ in range(10):
    case = input()
    stack = list(map(int, input().split()))
    front = 0
    cnt = 0

    while stack[front - 1] > 0:
        stack[front] -= cnt + 1
        front = (front + 1) % 8
        cnt = (cnt + 1) % 5

    stack[front - 1] = 0
    print("#{}".format(case), end=" ")
    print(*(stack[front:] + stack[:front]))

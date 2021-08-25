def my(num):
    queue = []
    count = [0]*20
    queue.append(1)
    board = [0]*20
    board[1] = 1
    while num > 0:
        a = queue.pop(0)
        count[a] += 1
        num -= count[a]
        queue.append(a)
        for i in range(1, 20):
            if board[i] == 0:
                queue.append(i)
                board[i] = 1
                break
    return a

n = 20
print(my(n))

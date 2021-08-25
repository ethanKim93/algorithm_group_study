import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    tc = input()
    data = list(map(int, input().split()))
    end = False
    while not end:
        for i in range(1, 6):
            new = data.pop(0)-i
            if new > 0:
                data.append(new)
            else:
                data.append(0)
                print('#{}'.format(tc), end=' ')
                print(*data)
                end = True


'''
# 망함
import sys
sys.stdin = open('input.txt')

# queue 함수
SIZE = 100
Q = [0] * SIZE
front, rear = -1, -1

# isFull
def is_full():
    global rear
    return rear == SIZE-1

# isEmpty
def is_empty():
    global front, rear
    return front == rear

# enQueue
def enqueue(item):
    global rear
    if is_full():
        print('Queue is full')
    else:
        rear += 1
        Q[rear] = item

# deQueue
def dequeue():
    global front
    if is_empty():
        return 'Queue is empty'
    else:
        front += 1
        return Q[front]

# Qpeek
def Qpeek():
    global front, rear
    if is_empty():
        return 'Queue is empty'
    else:
        return Q[front+1]


T = 10

for tc in range(1, T+1):
    tc = input()
    data = list(map(int, input().split()))
    for num in data:
        enqueue(num)
    print(Q)
    end = False
    while not end:
        for i in range(1, 6):
            new = dequeue()
            if new > 0:
                enqueue(new)
            else:
                enqueue(0)
                print('#{}'.format(tc), end=' ')
                print(*Q)
                end = True
    Q = [0] * SIZE
    front, rear = -1, -1
'''

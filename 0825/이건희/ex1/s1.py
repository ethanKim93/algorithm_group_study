example = [1,2,3]
front = -1
rear = -1
q = [0]*4

for i in example:
    rear += 1
    q[rear] = i

for i in range(3):
    front += 1
    print(q[front])
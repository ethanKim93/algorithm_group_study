def enqueue(item):
    global rear
    rear += 1
    Q[rear] = item

def dequeue():
    global front
    front += 1
    return Q[front]
# queue로 풀어보기
SIZE = 30
Q = [0] * SIZE
visit = [0] * (SIZE + 1)

front = rear = -1
tot = 0

start = True

for i in range(1, 20):
    if not start:
        enqueue(e)
    start = False
    enqueue(i)
    e = dequeue()
    visit[e] += 1
    tot += visit[e]
    print(Q)
    if tot > 20:
        break
print(e)

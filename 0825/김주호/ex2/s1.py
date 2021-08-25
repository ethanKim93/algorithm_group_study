queue = [0] * 20
cnt = {}

front = -1
rear = -1

who = 0
candy = 20
i = 1
while candy > 0:
    rear = (rear + 1) % 20
    queue[rear] = i
    print("큐에 있는 사람 수 :\n{}".format(rear - front if rear > front else rear - front + 20))
    print("현재 일인당 나눠주는 사탕의 수 :\n{}".format(cnt))
    print("현재까지 나눠준 사탕의 수 :\n{}".format(20 - candy))
    # print(queue)
    input()
    front = (front + 1) % 20
    who = queue[front]
    rear = (rear + 1) % 20
    queue[rear] = who
    if who not in cnt:
        cnt[who] = 1
    candy -= cnt[who]
    cnt[who] += 1
    i += 1
print("마지막 사탕은 {}번이 받아갔습니다!".format(who))

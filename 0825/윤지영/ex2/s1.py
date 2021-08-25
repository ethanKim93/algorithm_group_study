# N = 20  # 마이쮸 개수
# q = []  # 큐 생성
#
# mychew = [0] * 20
# now = 1
# cnt = 0
#
# while N > 0:
#     q.append(now)       #enQ
#     k = q.pop(0)
#     mychew[k] += 1  # 빠지는 번호 #deQ
#     N -= mychew[k]
#
#     q.append(k)
#
#     now += 1
#     cnt += mychew[k]
#
#     input()
#     print('큐에 있는 사람 수 :{}'.format(len(q)))
#     print('현재 일인당 나눠주는 사탕의 수 :{}'.format(k, mychew[k]))
#     print('현재까지 나눠준 사탕의 수:{}'.format(cnt))
# print()
# print('마지막에 받아간 사람 번호: {}'.format(k))

N = 20  # 마이쮸 개수
q = []  # 큐 생성

mychew = dict()
now = 1
cnt = 0

while N > 0:
    mychew[now] = 0
    q.append(now)       #enQ
    k = q.pop(0)
    mychew[k] += 1  # 빠지는 번호 #deQ
    N -= mychew[k]

    q.append(k)

    now += 1
    cnt += mychew[k]
    input()
    print('큐에 있는 사람 수 :{}'.format(len(q)))
    print('현재 일인당 나눠주는 사탕의 수 :{}'.format(mychew.items()))
    print('현재까지 나눠준 사탕의 수:{}'.format(cnt))
print()
print('마지막에 받아간 사람 번호: {}'.format(k))




# 20 번째로 마이쮸를 받아가는 사람은 누구?
candy = 20
q = [1]             # 처음 먹을 1번
nxt = 1
while 1:
    t = q.pop(0)    # 마이쮸 먹을 맨 처음 사람
    q.append(t)     # 먹자마자 줄섬
    candy -= 1      # t가 먹게됨
    nxt += 1        # 다음 사람
    q.append(nxt)   # 다음 사람 줄 섬
    if candy < len(q):  #남은 마이쮸 수가 기다리는 사람보다 작아질 때, 기다리는 사람의 인덱스 = 남은 마이쮸 수 -1
        print(q[candy-1])   #20번쨰로 먹는 사람은 3번
        break


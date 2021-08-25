chew = 20 # 마이쮸 갯수
mychew = [1]*20 # 각자 받을 마이쮸

q = [1] # 처음 줄
next = 2 # 다음 순서

while chew > 0:
    now = q.pop(0)
    chew -= mychew[now]
    mychew[now] += 1 # 받을 마이쮸 한 개 추가
    q.append(now) # 줄 뒤로 가기
    if mychew[now] >= 2: # 줄 뒤로 갔는데 받을 마이쮸가 2개 이상이면
        q.append(next) # 다음 순번 줄 뒤로
        next += 1 # 다음 사람 기다리기

print(now)
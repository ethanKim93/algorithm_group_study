'''
마이쮸 나눠주기 시뮬레이션
'''


def deQueue():
    return q.pop(0)


def enQueue(item):
    q.append(item)


q = [1]  # 줄 순서, 최초 1번으로 시작
person = 1  # 사람번호
total = 20  # 총 마이쮸
visited = [0, 1]        # 줄을 몇번째 서는지 체크, 1번 인덱스부터 사용하기 때문에 1번이
while total > 0:        # 20번째의 마이쮸를 가져가게 된다면 종료
    now = deQueue()     # 마이쮸를 받아갈 사람을 deQ
    visited[now] += 1   # 다음 줄을 설 때 한개씩을 더 받아야하기 때문에 방문횟수 추가
    person += 1
    enQueue(person)     #
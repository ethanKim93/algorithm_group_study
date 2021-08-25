'''
마이쮸 나눠주기 시뮬레이션
'''
def deQueue():
    return q.pop(0)
def enQueue(item):
    q.append(item)

q = [[1,0]]
person = 1      # 사람
total = 20      # 총 마이쮸
chew = 1       # 각 사람의 마이쮸, 1번부터시작하기위해 0번인덱스를 가진채로 초기화
while True:

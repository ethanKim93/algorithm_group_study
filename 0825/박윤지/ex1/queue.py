# 가변 큐를 만들라는 문제였는데 고정 큐를 만들었다. -> 교수님 코드 참고하기

"""
기본 Queue 구현 - 클래스 구현
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력
  (1, 2, 3을 차례대로 출력해야 함)
"""


class Queue:
    # 생성자 함수
    def __init__(self):
        self.q = [0] * 4
        self.front = -1
        self.rear = -1

    # isEmpty
    def is_empty(self):
        if self.rear == self.front:
            return True
        return False

    # enQueue
    def enqueue(self, item):
        self.rear += 1
        self.q[self.rear] = item

    # deQueue
    def dequeue(self):
        self.front += 1
        return self.q[self.front]

    # size
    def size(self):
        return self.rear - self.front

# 1. queue 인스턴스 생성
queue = Queue()
# 2. queue가 비었는지 확인
print(queue.is_empty())
# 3. 1, 2, 3 원소를 queue에 삽입
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
# 4. 원소가 정상적으로 삽입되었는지 확인 / 사이즈 확인 / 비었는지 여부 확인
print(queue.q)
print(queue.size())
print(queue.is_empty())
# 5. queue에서 원소 삭제 후 반환 & 원소 확인 / 사이즈 확인
print(queue.dequeue())
print(queue.size())
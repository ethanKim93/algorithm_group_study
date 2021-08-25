"""
기본 Queue 구현 - 클래스 구현
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력
  (1, 2, 3을 차례대로 출력해야 함)
"""


class Queue:
    # 생성자 함수
    def __init__(self):
        """
        인스턴스 생성 시에 새로운 Queue 생성
        """
        self.queue = [0] * 3
        self.front = -1
        self.rear = -1

    # isEmpty
    def is_empty(self):
        """
        Queue에 비어있는지 여부를 True / False로 반환
        """
        if len(self.queue) == 0:
            return True
        else:
            return False

    # enQueue 
    def enqueue(self, item):
        """
        Queue에 원소 삽입
        """
        self.rear += 1
        self.queue[self.rear] = item

        # deQueue

    def dequeue(self):
        """
        Queue에서 원소 삭제 후 반환
        """
        return self.queue.pop(0)

    # size
    def size(self):
        """
        Queue의 길이 반환
        """
        return len(self.queue)

# 1. queue 인스턴스 생성
Q = Queue()
# 2. queue가 비었는지 확인
print(Q.is_empty())
# 3. 1, 2, 3 원소를 queue에 삽입
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
# 4. 원소가 정상적으로 삽입되었는지 확인 / 사이즈 확인 / 비었는지 여부 확인
print(Q.queue)
print(Q.size())
print(Q.is_empty())
# 5. queue에서 원소 삭제 후 반환 & 원소 확인 / 사이즈 확인
print(Q.dequeue())  # 1
print(Q.size())
print(Q.dequeue())  # 2
print(Q.size())
print(Q.dequeue())  # 3
print(Q.size())
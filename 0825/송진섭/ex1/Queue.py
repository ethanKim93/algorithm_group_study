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
        self.datas = []
        self.front = self.rear = -1

    # isEmpty
    def is_empty(self):
        """
        Queue에 비어있는지 여부를 True / False로 반환
        """
        return self.datas == []

    # enQueue
    def enqueue(self, data):
        """
        Queue에 원소 삽입
        """
        self.datas.append(data)

        # deQueue

    def dequeue(self):
        """
        Queue에서 원소 삭제 후 반환
        """
        self.datas.pop(0)

    # size
    def size(self):
        """
        Queue의 길이 반환
        """
        return len(self.datas)


# 1. queue 인스턴스 생성
q1 = Queue()

# 2. queue가 비었는지 확인
print(q1.is_empty())

# 3. 1, 2, 3 원소를 queue에 삽입
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)

# 4. 원소가 정상적으로 삽입되었는지 확인 / 사이즈 확인 / 비었는지 여부 확인
print(q1.datas)
print(q1.size())
print(q1.is_empty())

# 5. queue에서 원소 삭제 후 반환 & 원소 확인 / 사이즈 확인
q1.dequeue()
print(q1.datas)
q1.dequeue()
print(q1.datas)
q1.dequeue()
print(q1.datas)
print(q1.size())

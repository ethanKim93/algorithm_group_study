"""
기본 Queue 구현 - 클래스 구현
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력
  (1, 2, 3을 차례대로 출력해야 함)
"""

class Queue:
    # 생성자 함수
    def __init__(self, length):
        """
        인스턴스 생성 시에 새로운 Queue 생성
        """
        self.data = []
        print("Queue Constructed")

    # isEmpty
    def is_empty(self):
        """
        Queue에 비어있는지 여부를 True / False로 반환
        """
        if self.data :
            print("Queue is not Empty")
            return False
        print("Queue is Empty")
        return True

    # enQueue
    def enqueue(self, item):
        """
        Queue에 원소 삽입
        """
        self.data.append(item)

    # deQueue
    def dequeue(self):
        """
        Queue에서 원소 삭제 후 반환
        """
        if not self.data :
            print("Queue is Empty")
            return
        return self.data.pop(0)


    # size
    def size(self):
        """
        Queue의 길이 반환
        """
        print("size of the queue is {}".format(len(self.data)))
        return len(self.data)

    def __str__(self):
        return " ".join(map(str, self.data))

# 1. queue 인스턴스 생성
queue = Queue(3)
print()
# 2. queue가 비었는지 확인
queue.is_empty()
# 3. 1, 2, 3 원소를 queue에 삽입
queue.enqueue(1)
print(queue)
queue.enqueue(2)
print(queue)
queue.enqueue(3)
print(queue)
print()
# 4. 원소가 정상적으로 삽입되었는지 확인 / 사이즈 확인 / 비었는지 여부 확인
print(queue)
queue.size()
queue.is_empty()
print()
# 5. queue에서 원소 삭제 후 반환 & 원소 확인 / 사이즈 확인
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
print()
print(queue)
queue.size()
queue.is_empty()



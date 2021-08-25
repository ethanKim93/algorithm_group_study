# 클래스를 활용한 선형 큐 구현

class Queue:
    # 생성자 함수
    def __init__(self, length):
        """
        인스턴스 생성 시에 새로운 Queue 생성
        """
        self.front = -1
        self.rear = -1
        self.length = length
        self.data = [0] * self.length
        print("Queue Constructed")

    # isEmpty
    def is_empty(self):
        """
        Queue에 비어있는지 여부를 True / False로 반환
        """
        if self.rear == self.front :
            print("Queue is Empty")
            return True
        print("Queue is not Empty")
        return False

    #isFull
    def is_full(self):
        """
        Queue가 꽉 차있는지 여부를 True / False로 반환
        """
        if self.rear == self.length - 1:
            print("Queue is Full")
            return True
        print("Queue is not Full")
        return False

    # enQueue
    def enqueue(self, item):
        """
        Queue에 원소 삽입
        """
        if self.rear == self.length - 1:
            print("Queue is Full")
            return
        self.rear += 1
        self.data[self.rear] = item

    # deQueue
    def dequeue(self):
        """
        Queue에서 원소 삭제 후 반환
        """
        if self.rear == self.front :
            print("Queue is Empty")
            return
        self.front += 1
        return self.data[self.front]

    def __str__(self):
        return " ".join(map(str, self.data))

# 1. queue 인스턴스 생성
queue = Queue(3)
print()
# 2. queue가 비었는지 확인
queue.is_empty()
# 3. 1, 2, 3 원소를 queue에 삽입
print(queue)
queue.enqueue(1)
print(queue)
queue.enqueue(2)
print(queue)
queue.enqueue(3)
print(queue)
print()
# 4. 원소가 정상적으로 삽입되었는지 확인 / 사이즈 확인 / 비었는지 여부 확인
queue.is_empty()
queue.is_full()
print()
# 5. queue에서 원소 삭제 후 반환 & 원소 확인 / 사이즈 확인
print(queue, queue.dequeue())
print(queue, queue.dequeue())
print(queue, queue.dequeue())
print(queue)
print()
queue.is_empty()
queue.is_full()
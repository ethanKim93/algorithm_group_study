class Queue:

    # 생성자 함수
    def __init__(self):
        """
        인스턴스 생성 시에 새로운 Queue 생성
        """
        self.queue = []

    # isEmpty
    def is_empty(self):
        """
        Queue에 비어있는지 여부를 True / False로 반환
        """
        return self.queue == []

    # enQueue
    def enqueue(self, item):
        """
        Queue에 원소 삽입
        """
        self.queue.append(item)

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


queue = Queue()

print(queue.is_empty())

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.queue)
print(queue.size())
print(queue.is_empty())
print(queue.dequeue())
print(queue.queue)
print(queue.dequeue())
print(queue.queue)
print(queue.dequeue())
print(queue.queue)
print(queue.is_empty())


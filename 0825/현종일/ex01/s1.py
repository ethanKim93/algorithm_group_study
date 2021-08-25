from queue import Queue

# 1. queue 인스턴스 생성
q1 = Queue()
# 2. queue가 비었는지 확인
print(q1.is_empty())
# 3. 1, 2, 3 원소를 queue에 삽입
a = [3, 1, 2, 3]
for n in a:
    q1.enqueue(n)
# 4. 원소가 정상적으로 삽입되었는지 확인 / 사이즈 확인 / 비었는지 여부 확인
print(q1.queue)
print(q1.size())
print(q1.is_empty())
# 5. queue에서 원소 삭제 후 반환 & 원소 확인 / 사이즈 확인
for _ in range(2):
    print(q1.dequeue())
    print(q1.size())
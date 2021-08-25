person = 1
candy = 20
queue = []
queue.append([person, 0])       # 1번 enQ
while candy:                    # 마이쮸가 떨어질 때까지 반복
    temp = queue.pop(0)         # 큐의 첫번째 사람 deQ
    temp[1] += 1                # 마이쮸 받기
    candy -= 1                  # 마이쮸 재고 -1
    queue.append(temp)          # 마이쮸 받은 사람 다시 줄서기
    person += 1                 # 추가될 사람 번호 +1
    queue.append([person, 0])   # 새로운 사람 줄서기
print(queue[-2][0])             # 큐의 뒤에서 두번째 사람이 마지막 마이쮸를 받는다
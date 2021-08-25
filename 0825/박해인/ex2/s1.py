# 20개의 마이쮸가 있을 때 마지막 것을 누가 가져갈까?
mychew = 20
queue = []
count = {1: 0}  # 누가 몇 개 가져갔는지 셀 딕셔너리
i = 0

while True:
    # 사람 추가
    i += 1
    queue.append(i)
    # 맨 앞사람이 마이쮸를 가져간다
    # 재방문시 사탕 챙기는 갯수 + 1
    again = queue.pop(0)

    try:
        count[again] += 1
    except:
        count.update({again: 1})
    mychew -= count[again]

    # 뒤로 간다
    queue.append(again)

    # mychew가 0개 이하로 떨어지면 가져간 사람 print
    if mychew <= 0:
        print('{}번이 마지막 마이쮸를 가져갔다!!!!!!'.format(again))
        break

# 각각 몇 개 가져갔는지
for i, mychew in count.items():
    total = 0
    while mychew != 0:
        total += mychew
        mychew -= 1
    print('{}번이 {}개를 가져갔다'.format(i, total))

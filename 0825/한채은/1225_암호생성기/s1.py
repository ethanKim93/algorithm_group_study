import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = input()
    data = list(map(int, input().split()))

    acc = 1
    while True:
        # 빼는 값이 5보다 클 때
        if acc > 5:
            acc = 1
        new_data = data.pop(0) - acc
        acc += 1

        # 바뀔 data가 0보다 작아졌을 때
        if new_data <= 0:
            new_data = 0
            data.append(new_data)
            break

        data.append(new_data)

    print('#{} {}'.format(tc, *data))
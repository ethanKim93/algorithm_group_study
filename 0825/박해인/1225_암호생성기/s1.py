import sys
sys.stdin = open('input.txt')

for _ in range(1):
    test_case = int(input())
    data = list(map(int, input().split()))

    i = 1  #뺄 숫자

    while True:
        if data[0] - i > 0:
            data.append(data.pop(0)-i)
        else:
            data.pop(0)
            data.append(0)

        if i == 5:
            i = 1
        else:
            i += 1

        if data[-1] == 0:
            break

    print('#{} {}'.format(test_case, " ".join(map(str, data))))
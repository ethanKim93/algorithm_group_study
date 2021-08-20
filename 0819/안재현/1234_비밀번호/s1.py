import sys

sys.stdin = open("input.txt")


def popping(empty):
    for j in range(len(empty) - 1):
        if empty[j] == empty[j + 1]:
            empty.pop(j)
            empty.pop(j)
            return popping(empty)
    return empty


for tc in range(0, 10):
    T, N = input().split()
    empty = []
    for i in str(N):
        empty.append(i)
    print('#{} '.format(tc + 1), end='')
    for j in range(len(popping(empty))):
        print('{}'.format(popping(empty)[j]), end='')
    print()
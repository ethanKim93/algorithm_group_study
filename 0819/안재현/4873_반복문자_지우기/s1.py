import sys

sys.stdin = open("sample_input.txt")


def popping(empty):
    for j in range(len(empty) - 1):
        if empty[j] == empty[j + 1]:
            empty.pop(j)
            empty.pop(j)
            return popping(empty)
    return empty


T = int(input())
for tc in range(0, T):
    N = input()
    empty = []
    for i in range(len(N)):
        empty.append(N[i])
    print('#{} {}'.format(tc + 1, len(popping(empty))))
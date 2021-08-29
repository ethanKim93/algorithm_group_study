import sys
sys.stdin = open('input.txt')


def search(x):
    global result

    if len(Child[x]):
        search(Child[x][0])

    result += String[x][0]

    if len(Child[x]) == 2:
        search(Child[x][1])


for TC in range(1, 11):
    T = int(input())

    Child = [[] for _ in range(T + 1)]

    String = [[] for _ in range(T + 1)]
    for _ in range(T):
        Input = list(input().split())

        String[int(Input[0])].append(Input[1])

        if len(Input) >= 3:
            Child[int(Input[0])].append(int(Input[2]))
        if len(Input) == 4:
            Child[int(Input[0])].append(int(Input[3]))

    result = ''
    search(1)
    print("#{} {}".format(TC, result))
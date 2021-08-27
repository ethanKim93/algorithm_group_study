import sys
sys.stdin = open("sample_input.txt")

for case in range(int(input())):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))

    queue = [pizza[i] for i in range(N)]
    firepit = [i for i in range(N)]
    welldone = 0
    front = -1

    last = 0

    while welldone < M:
        front = (front + 1) % len(queue)
        if queue[front] != -1:
            queue[front] //= 2
            if queue[front] == 0:
                last = firepit[front]
                welldone += 1
                if N + welldone <= M:
                    queue[front] = pizza[N + welldone - 1]
                    firepit[front] = N + welldone - 1
                else:
                    queue[front] = -1

    print("#{} {}".format(case + 1, last + 1))
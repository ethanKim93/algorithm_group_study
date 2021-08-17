import sys
sys.stdin = open("test_input.txt", "rt", encoding="UTF8")

for _ in range(10):
    N = int(input())
    find = input()
    search = input()
    total = 0

    for i in range(len(search) - len(find) + 1):
        cnt = 0

        for j in range(len(find)):
            if search[i + j] != find[j]:
                break
            cnt += 1

        if cnt == len(find):
            total += 1

    print("#{} {}".format(N, total))
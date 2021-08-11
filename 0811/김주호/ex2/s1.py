import sys
sys.stdin = open("input.txt")

for case in range(int(input())):
    arr = list(map(int, input().split()))

    flag = False
    for i in range(1 << 10):
        li = []
        for j in range(11):
            if i & (1 << j):
                li.append(arr[j])

        if len(li) and sum(li) == 0:
            flag = True
            break

    print("#{} {}".format(case + 1, 1 if flag else 0))
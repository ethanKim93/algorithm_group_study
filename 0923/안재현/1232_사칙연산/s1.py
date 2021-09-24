import sys

sys.stdin = open('input.txt')


def tree(val):
    if val[1] == '+':
        return tree(arr[int(val[2])]) + tree(arr[int(val[3])])
    elif val[1] == '-':
        return tree(arr[int(val[2])]) - tree(arr[int(val[3])])
    elif val[1] == '*':
        return tree(arr[int(val[2])]) * tree(arr[int(val[3])])
    elif val[1] == '/':
        return tree(arr[int(val[2])]) / tree(arr[int(val[3])])
    else:
        return int(val[1])


for t in range(1, 11):
    n = int(input())
    arr = [0]
    for _ in range(n):
        arr.append(input().split())

    print("#{} {}".format(t, int(tree(arr[1]))))
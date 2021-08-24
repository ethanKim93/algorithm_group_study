import sys
sys.stdin = open('sample_input.txt')


def fight(a, b):
    if (students[a-1] - students[b-1]) % 3 < 2:
        return a
    return b


def matches(start, end):
    if start == end:
        return start

    left = matches(start, (start+end)//2)
    right = matches((start+end)//2+1, end)
    return fight(left, right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    students = list(map(int, input().split()))
    print(matches(1, N))

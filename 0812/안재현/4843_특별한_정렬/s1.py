import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(0, T):
    N = int(input())
    A = list(map(int, input().split()))
    New = []
    switch = 0
    result = ""
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
#    print(A)
    for i in range(0, 5):
            New.append(A[i])
            New.append(A[len(A) - switch-1])
            switch += 1
    for j in range(0, len(New), 2):
        key = New[j]
        New[j] = New[j+1]
        New[j + 1] = key

    for k in range(len(New)):
        result += (str(New[k]) + " ")

    print("#{} {}".format(tc+1, result))

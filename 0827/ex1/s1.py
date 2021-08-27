def check_front(n):
    if n:
        print(n, end=" ")
        check_front(left[n])
        check_front(right[n])
    return
def check_middle(n):
    if n:
        check_middle(left[n])
        print(n, end=" ")
        check_middle(right[n])
    return
def check_back(n):
    if n:
        check_back(left[n])
        check_back(right[n])
        print(n, end=" ")
    return

input = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'

edges = list(map(int, input.split()))
N = 13
left = [0] * (N + 1)
right = [0] * (N + 1)

for i in range(0, len(edges), 2):
    if left[edges[i]] == 0:
        left[edges[i]] = edges[i+1]
    else:
        right[edges[i]] = edges[i+1]

check_front(1)
print()
check_middle(1)
print()
check_back(1)
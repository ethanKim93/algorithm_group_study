import sys
sys.stdin = open("input.txt")

def quick_sort(li):
    if len(li) <= 1:
        return li

    pivot = li[0]
    remainder = li[1:]

    left = [x for x in remainder if x <= pivot]
    right = [x for x in remainder if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    maps = list(map(int,input().split()))
    A = quick_sort(maps)

    print("#{} {}".format(tc, A[n//2]))

# Fail: Time over
import sys
sys.stdin = open("sample_input.txt")


def quick(start, end):
    if end - start <= 1:
        return

    front = start
    rear = front - 1
    pivot = end - 1

    while front < end:
        if nums[front] <= nums[pivot]:
            rear += 1
            nums[rear], nums[front] = nums[front], nums[rear]

        front += 1

    quick(start, rear)
    quick(rear + 1, end)


for case in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))
    quick(0, N)
    print("#{} {}".format(case + 1, nums[N//2]))

import sys
sys.stdin = open('sample_input.txt')

# 최종 코드(김주호)
def quick(start, end):
    # end - start 인덱스가 1이하면 바로 return
    if end - start <= 1:
        return

    # 시작하는 친구
    front = start
    # 뒤따라오는 친구
    rear = front - 1
    # 가장 오른쪽 수가 pivot
    pivot = end - 1

    while front < end:
        # front보다 pivot이 크면
        if nums[front] <= nums[pivot]:
            # 뒤따라 오는 친구 + 1 해주고
            rear += 1
            # 자리 바꿔주기
            nums[rear], nums[front] = nums[front], nums[rear]

        # 아니면 rear은 못움직이고 front만 움직이기
        front += 1

    # 피벗보다 작은 녀석이면 front랑 rear랑 가르키는 녀석이 같아짐
    # 그럼 두개 바꿔봤자 자기 자신이니까 배열에 변화가 없음

    # 마지막 rear 기준 왼쪽
    quick(start, rear)
    # 마지막 rear 기준 오른쪽
    quick(rear + 1, end)


for case in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))
    quick(0, N)
    print("#{} {}".format(case + 1, nums[N//2]))
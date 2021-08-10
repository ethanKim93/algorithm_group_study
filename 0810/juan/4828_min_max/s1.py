import sys
sys.stdin = open('sample_input.txt')

# bubble sort 를 함수화
# 함수 사용시 호출보다 먼저 함수가 선언되어야 하기때문에 파일 상단에 작성

def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    bubble_sort(nums)
    ans = nums[N-1] - nums[0]
    print('#{} {}'.format(tc, ans))
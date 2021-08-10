import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    for i in range(len(nums)-1, 0, -1):
        for j in range(0, i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                #버블정렬
    #print(nums[-1] - nums[0]) #끝 값 빼기
    print('#{0} {1}'.format(tc,nums[-1] - nums[0]))









    # print('#{} {}'.format(tc, total))
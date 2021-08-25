import sys
sys.stdin = open("sample_input.txt")
'''
주호님 코드보고 재귀로 접근
'''
def div(nums, keys):    #nums는 낸 수 1, 2, 3 중 // keys는 각 사람의 인덱스
    n = len(nums)
    if n >2 :       # 두명 이상이면 재귀로 사람 나눔
        n1, k1 = div(nums[:(n+1)//2], keys[:(n+1)//2])
        n2, k2 = div(nums[(n+1)//2:], keys[(n+1)//2:])
        return div([n1, n2], [k1, k2])
    elif n==2:
        if nums in right_win:
            return nums[1], keys[1]
        else:
            return nums[0], keys[0]
    else:
        return nums[0], keys[0]


for tc in range(1, int(input())+1):
    N = int(input())
    nums = list(map(int,input().split()))
    keys = range(1,len(nums)+1)
    right_win = [[3, 1], [1, 2], [2, 3]]
    print('#{} {}'.format(tc, div(nums, keys)[1]))


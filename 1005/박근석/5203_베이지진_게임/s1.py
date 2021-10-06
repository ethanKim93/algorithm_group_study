import sys
sys.stdin = open('input.txt')

T = int(input())

def check(x, num):
    if x[num] == 3:
        return True

    if num > 1 and x[num - 1] and x[num - 2]:
        return True
    if num < 9 and x[num + 1] and x[num + 2]:
        return True
    if num and not num==9 and x[num + 1] and x[num - 1]:
        return True
    return False


for tc in range(1, T + 1):
    nums = list(map(int, input().split()))
    a = 10*[0]
    b = 10*[0]
    answer = 0
    flag = 0
    for i in range(len(nums)):
        if i%2:
            b[nums[i]] += 1
            if check(b, nums[i]):
                answer = 2
                break
        else:
            a[nums[i]] += 1
            if check(a, nums[i]):
                answer = 1
                break
    print('#{} {}'.format(tc, answer))



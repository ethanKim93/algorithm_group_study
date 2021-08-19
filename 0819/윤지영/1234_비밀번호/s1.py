import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1,T+1):
    li = input().split()
    N, nums = int(li[0]), li[1]
    stack = []
    for num in nums:
        if (not stack) or (num != stack[-1]):
            stack.append(num)
        else:
            stack.pop()
    print('#{} {}'.format(tc, ''.join(stack)))
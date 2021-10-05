import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    nums, k = input().split()
    N = len(nums)
    num = set([nums])  # 중복제거
    com = set()
    k = int(k)

    for _ in range(k):
        while num:
            a = list(num.pop())
            for i in range(N):  # powerset 방식
                for j in range(i+1, N):
                    a[i], a[j] = a[j], a[i]
                    com.add(''.join(a))
                    a[i], a[j] = a[j], a[i]
        num, com = com, num  # k만큼 교체 해주면서 모든 경우의 수를 더한다.

    print('#{} {}'.format(tc, max(num)))

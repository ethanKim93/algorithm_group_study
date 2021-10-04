import sys
sys.stdin = open('input.txt')


# def dfs(change):
#     global maxV
#     if not change:
#         temp = int(''.join(num_list))
#         if maxV < temp:
#             maxV = temp
#         return
#     for i in range(len_num):
#         for j in range(i+1, len_num):
#             num[i], num[j] = num[j], num[i]
#             temp_key = ''.join(num_list)
#             if temp_key in visited:
#                 ######
#                 dfs(change-1)
#             num[i], num[j] = num[j], num[i]
#
#
#
#
#
#
T = int(input())
for tc in range(1, T+1):
    num, cnt = input().split()  # 숫자판의 정보, 교환횟수
    K = int(cnt)
    N = len(num)
    now = set([num])

    nxt = set()

    for _ in range(cnt):
        while now:
            s = now.pop()
            s = list(s)
            for i in range(N):
                for j in range(i+1,N):
                    s[i], s[j] = s[j], s[i]
                    nxt.add(''.join(s))
                    s[i], s[j] = s[j], s[i]
        now, nxt = nxt, now

    print('#{} {}'.format(tc, max(map(int, now))))
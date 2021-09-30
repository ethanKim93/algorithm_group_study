import sys
sys.stdin = open('sample_input.txt', 'r')
#
# # 2진수 dict
# binary = {
#     '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
#     '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
#     'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
# }
#
# # 암호코드 dict
# code = {
#     (2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2): 2, (4, 1, 1): 3, (1, 3, 2): 4,
#     (2, 3, 1): 5, (1, 1, 4): 6, (3, 1, 2): 7, (2, 1, 3): 8, (1, 1, 2): 9,
# }
#
# T = int(input())
# for tc in range(1, T + 1):
#     # N = 세로, M = 가로
#     N, M = map(int, input().split())
#
#     # 중복 제거, 0만 있는 배열 제거
#     arr = sorted(list(set([input()[:M] for _ in range(N)])))
#
#     last = 0
#     visited = []
#     arr.pop(0)
#
#     # 2진수 변환
#     for i in range(len(arr)):
#         result = ''
#         for j in range(len(arr[i])):
#             result += binary[arr[i][j]]
#
#         # result 의 오른쪽 0 제거
#         result = result.rstrip('0')
#
#         # 0, 1을 이용해서 숫자 찾기
#         ze_one = []
#
#         n1 = n2 = n3 = n4 = 0
#         for k in range(len(result)-1, -1, -1):
#             if result[k] == '1' and n3 == 0:
#                 n4 += 1
#             elif result[k] == '0' and n2 == 0:
#                 n3 += 1
#             elif result[k] == '1' and n1 == 0:
#                 n2 += 1
#             elif result[k] == '0':
#                 if result[k - 1] == '1':
#                     n = min(n2, n3, n4)
#                     ze_one.append((code[n2 // n, n3 // n, n4 // n]))
#                     n2 = n3 = n4 = 0
#                     if len(ze_one) == 8:
#                         if not ((ze_one[1] + ze_one[3] + ze_one[5] + ze_one[7]) * 3
#                                 + ze_one[0] + ze_one[2] + ze_one[4] + ze_one[6]) % 10:
#                             if ze_one not in visited:
#                                 last += sum(ze_one)
#                                 visited.append(ze_one)
#                         ze_one = []
#     print('#{} {}'.format(tc, last))
Bi = {
    '0':'0000', '1':'0001', '2':'0010', '3':'0011',
    '4':'0100', '5':'0101', '6':'0110', '7':'0111',
    '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
    'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'
}

code = {
    '211':0, '221':1, '122':2, '411':3,
    '132':4, '231':5, '114':6, '312':7,
    '213':8, '112':9
}


def rate(x, y, z):
    min_num = min(x,y,z)
    x //= min_num
    y //= min_num
    z //= min_num
    return str(x)+str(y)+str(z)


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    print(arr)

    Bi_list = [''] * N
    for i in range(N):
        for j in range(M):
            Bi_list[i] += Bi[arr[i][j]]
    print(Bi_list)

    codes, total, visited = [], 0, []
    for r in range(N):
        cnt_1, cnt_2, cnt_3 = 0, 0, 0
        for c in range(M * 4 - 1, -1, -1):
            if cnt_2 == 0 and cnt_3 == 0 and Bi_list[r][c] == '1':
                cnt_1 += 1
            elif cnt_1 > 0 and cnt_3 == 0 and Bi_list[r][c] == '0':
                cnt_2 += 1
            elif cnt_1 > 0 and cnt_2 > 0 and Bi_list[r][c] == '1':
                cnt_3 += 1
            print(cnt_1, cnt_2, cnt_3)
            if cnt_1 > 0 and cnt_2 > 0 and cnt_3 > 0 and Bi_list[r][c] == '0':
                codes.append(code[rate(cnt_3, cnt_2, cnt_1)])
                cnt_1, cnt_2, cnt_3 = 0, 0, 0

            if len(codes) == 8:
                codes = codes[::-1]
                check = (codes[0] + codes[2] + codes[4] + codes[6]) * 3 + (codes[1] + codes[3] + codes[5] + codes[7])

                if check % 10 == 0 and codes not in visited:
                    total += sum(codes)
                visited.append(codes)
                codes = []
    print("#{} {}".format(tc, total))

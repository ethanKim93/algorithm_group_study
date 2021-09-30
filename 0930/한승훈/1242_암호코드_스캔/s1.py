import sys
sys.stdin = open('sample_input.txt')

password = {'211':0, '221':1, '122':2, '411':3, '132':4, '231':5, '114':6, '312':7, '213':8, '112':9}
hex = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    codes = list(set([input() for _ in range(N)]))
    bi = [''] * N
    ans = 0

    for i in range(len(codes)):
        for j in range(M):
            bi[i] += hex[codes[i][j]]  # 16진수를 2진수로 바꿔서 co 리스트에 담기
    code_lst = []
    visited = []
    for x in range(N):
        c1 = c2 = c3 = c4 = 0
        if len(bi[x]) == M*4:
            for y in range(M*4-1, -1, -1):
                if bi[x][y] == '1' and not c3 and not c2:
                    c4 += 1
                elif bi[x][y] == '0' and not c2 and c4:
                    c3 += 1
                elif bi[x][y] == '1' and c3 and c4:
                    c2 += 1
                elif bi[x][y] == '0' and c2 and c3 and c4:
                    n = min(c2, c3, c4)
                    c2 = str(c2 // n)
                    c3 = str(c3 // n)
                    c4 = str(c4 // n)
                    code_lst.append(password[c2+c3+c4])
                    c2 = c3 = c4 = 0

                    if len(code_lst) == 8:
                        odd = even = 0
                        code_lst = code_lst[::-1]
                        for u in range(0, 7, 2):
                            odd += code_lst[u]
                        for v in range(1, 8, 2):
                            even += code_lst[v]
                        if not (odd * 3 + even) % 10 and code_lst not in visited:
                            ans += sum(code_lst)
                        visited.append(code_lst)
                        code_lst = []

    print('#{} {}'.format(tc, ans))












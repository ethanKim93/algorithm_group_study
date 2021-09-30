from math import gcd

import sys
sys.stdin = open('sample_input (1).txt')

check = {
    '3:2:1:1' : 0, '2:2:2:1' : 1, '2:1:2:2':2, '1:4:1:1':3, '1:1:3:2':4, '1:2:3:1':5, '1:1:1:4':6, '1:3:1:2':7,
    '1:2:1:3' : 8, '3:1:1:2' : 9
}

def bin_count(r,c, board):
    cnt1 = cnt2 = cnt3 = cnt4= 0
    flag1= flag2 = flag3 = flag4 = True
    while c > -1:
        if board[r][c] == '1' :
            if cnt3:
                flag3 = False
            if cnt1:
                break
            if flag4 is True:
                cnt4 += 1
            elif flag2 is True:
                cnt2 += 1
        elif board[r][c] == '0':
            if cnt4 :
                flag4 = False
            if cnt2 :
                flag2 = False
            if flag3 is True:
                cnt3 += 1
            elif flag1 is True:
                cnt1 += 1
        c -= 1
    return cnt1,cnt2,cnt3,cnt4

def gcd_4(c1,c2,c3,c4):
    times = gcd(gcd(c1, c2), gcd(c3, c4))
    c1 = str(c1//times)
    c2 = str(c2//times)
    c3 = str(c3//times)
    c4 = str(c4//times)
    return c1+':'+c2+':'+c3+':'+c4

def find_start():
    i= 0
    while i < N:
        j = (M*4)-1
        while j > -1:
            if new_li[i][j] == '1':
                # 첫 패턴의 비율
                cnt1, cnt2, cnt3, cnt4 = bin_count(i,j, new_li)
                # 다 더하면 한 글자의 길이 수가 되는것
                char_len = cnt1+cnt2+cnt3+cnt4
                code_len = char_len * 8
                n = new_li[i][j-code_len+1:j+1]
                if n not in num:
                    num.append(n)
                    num.append(char_len)
                j -= code_len +1
            j -= 1
        i += 1

# 16진수의 각 값을 2진수로 변환
def Bbit_print(n):
    output = ''
    for j in range(3,-1,-1):
        output += '1' if n & (1<<j) else '0'
    return output

# 암호코드 유효성 검사
def vaild(n):
    ans_2 = ans_1 = 0
    for i in range(len(n)):
        if i%2 == 0:
            ans_2 += int(n[i])
        else:
            ans_1 += int(n[i])
    ans = ans_2 * 3 + ans_1
    if ans % 10 == 0:
        return True
    else:
        return False


T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    li = [input() for _ in range(N)]
    new_li = ['' for _ in range(N)]
    num = []
    for i in range(N):
        for j in range(M):
            new_li[i] += Bbit_print(int(li[i][j],16))
    find_start()
    code_char = [[] for _ in range(len(num)//2)]
    result = ['' for _ in range(len(num)//2)]
    m = r = 0
    for j in range(0,len(num),2):
        code, char_len = num[j], num[j+1]
        for k in range(0,len(code),char_len):
            code_char[m].append(code[k:k+char_len])
        m += 1
    for char in code_char:
        for c in range(8):
            c1,c2,c3,c4 = bin_count(c,len(char[0])-1,char)
            result[r] += str(check[gcd_4(c1,c2,c3,c4)])
        r+=1
    ans = 0
    for r in result:
        if vaild(r) is True:
            ans += sum(list(map(int,r)))
        else:
            ans += 0
    print('#{} {}'.format(tc, ans))






# 16진수를 먼저 찾은 다음에 2진수로 바꿔서 계산하려했는데, 그렇게 하려니까 2진수로 바꾼다음에 어디서부터 시작이고 끝인지 찾을때 고려해야할게 너무 많아서 방법 변경
# check = {
#     '3:2:1:1' : 0, '2:2:2:1' : 1, '2:1:2:2':2, '1:4:1:1':3, '1:1:3:2':4, '1:2:3:1':5, '1:1:1:4':6, '1:3:1:2':7,
#     '1:2:1:3' : 8, '3:1:1:2' : 9
# }
#
# def find_end(m,n):
#     for k in range(n, -1, -1):
#         if k-4 >= 0:
#             if li[m][k-4:k] == '0000':
#                 end.append([m, k])
#                 return k-1
#         else:
#             if li[m][0:k] == '0' * k :
#                 end.append([m,k])
#                 return k-1
#
# def find_start():
#     i= 0
#     while i < N:
#         j = M-1
#         while j != 0:
#             if li[i][j] != '0':
#                 start.append([i,j])
#                 e = find_end(i,j)
#                 j = e +1
#             j -= 1
#         i += 1
#
# # 16진수의 각 값을 2진수로 변환
# def Bbit_print(n):
#     output = ''
#     for j in range(3,-1,-1):
#         output += '1' if n & (1<<j) else '0'
#     return output
#
# # 암호코드 유효성 검사
# def vaild(n):
#     ans_2 = ans_1 = 0
#     for i in range(len(n)):
#         if i%2 == 0:
#             ans_2 += n[i]
#         else:
#             ans_1 += n[i]
#     ans = ans_2 * 3 + ans_1
#     if ans % 10 == 0:
#         return True
#     else:
#         return False
#
# # 2진수에서 각 0과 1 비율구하기
# def count_bin(n):
#     cnt1 = cnt2 = cnt3= cnt4 = 0,0,0,0
#     flag1 = flag2 = flag3 = flag4 =True,True,True,True
#     for i in range(len(n)):
#         if n[i] == '0' and flag1 is True:
#            cnt1 += 1
#         elif n[i] =='1' and flag2 is True:
#             flag1 = False
#             cnt2 += 1
#         elif n[i] =='0' and flag3 is True:
#             flag2 = False
#             cnt3 += 1
#         elif n[i] =='1' and flag4 is True:
#             flag3 = False
#             cnt4 += 1
#
# T = int(input())
# for tc in range(1,T+1):
#     N,M = map(int,input().split())
#     li = [input() for _ in range(N)]
#     start = []
#     end = []
#     find_start()
#     num_list = []
#     result = []
#     for k in range(len(start)):
#         num = li[start[k][0]][end[k][1]:start[k][1]+1]
#         if num not in num_list:
#             num_list.append(num)
#     for bit in num_list:
#         ans = ''
#         for k in range(len(bit)):
#             ans += Bbit_print(int(bit[k], 16))
#         result.append(ans)
#         print(ans)
#     for m in range(len(result)):
#         ans = result[m]
#         char_len = len(ans)//8
#         bin_list = []
#         j = 0
#         for _ in range(8):
#             bin_list.append(result[m][j:j+char_len])
#             j += char_len
#         print(bin_list)




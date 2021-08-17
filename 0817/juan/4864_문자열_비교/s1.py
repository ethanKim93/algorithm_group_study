T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    for i in range(len(str2)-len(str1)+1):
        if str2[i:i+len(str1)] == str1:     # str2 문자열을 고지식하게 순회하며 str1과 일치하는 문자열 검색
            print('#{} 1'.format(tc))
            break                           # 찾았으면 더이상 순회할 필요없이 종료
    else:                                   # 순회를 다 돌아도 찾지못한 경우
        print('#{} 0'.format(tc))
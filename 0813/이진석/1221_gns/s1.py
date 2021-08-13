import sys

sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    casenum, case = input().split()  # 케이스번호, 문자열의 길이
    string = input()  # 비교대상 문자열
    compare_case = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']  # 비교를 위한 문자열
    answer = [] # ZRO~NIN 까지 순서대로 문자열을 담을 배열

    for i in range(10): # 0 ~ 9
        for j in range(0, len(string), 4):  # 공백 포함 4칸씩 비교하면서 compare_case와 비교
            if compare_case[i] == string[j:j + 3]:
                answer.append(compare_case[i])
    print(casenum)
    print(*answer)

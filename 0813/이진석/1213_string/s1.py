import sys
sys.stdin = open('input.txt', 'r', encoding='UTF8')

for _ in range(10):
    N = int(input())    # 테스트케이스 번호
    target = input()    # 찾을 문자열
    string = input()    # 검색할 문장
    i = 0   # 순회를 돌기위한 변수
    flag = 0    # 비교중인 첫 문자가 같다면 이후 반복문을 실행하기 위한 변수
    answer = 0  # 일치하는 횟수를 담을 변수
    while i < (len(string)-len(target)+1):  # 첫글자부터 비교하기 때문에 target의 첫글자를 뺀 나머지 글자수 만큼은 비교X
        if string[i] == target[0]:      # 첫 글자가 같다면
            flag = 1
            for j in range(len(target)):    # 반복문실행 ( 나머지 문자 비교)
                if flag:
                    if string[i+j] == target[j]:
                        continue
                    else :
                        flag = 0
                        break
        if flag:
            answer += 1
            i += len(target)
        else:
            i += 1
        flag = 0


    print('#{} {}'.format(N, answer))
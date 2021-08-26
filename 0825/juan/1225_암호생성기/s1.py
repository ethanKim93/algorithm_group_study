import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    tc = input()
    password = list(map(int, input().split()))

    while password[-1]:                                         # password의 마지막 항목에 0이 아닌 값이 있는 동안 반복
        for i in range(1,6):                                    # 1~5까지 사이클을 돌기 위한 반복문
            first = password.pop(0)                             # password의 첫항목 꺼내서
            if first - i > 0:                                   # i만큼 뺀 이후에도 0보다 크면
                password.append(first-i)                        # 그대로 password 마지막에 추가
            else:                                               # i만큼 뺐더니 0보다 작거나 같으면
                password.append(0)                              # password 마지막에 0을 추가하고 반복 중단
                break
    print('#{} {}'.format(tc, ' '.join(map(str, password))))

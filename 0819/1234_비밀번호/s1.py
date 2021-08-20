import sys
<<<<<<< HEAD

sys.stdin = open("input.txt")

for tc in range(1, 11):
    n, text = input().split()
    n = int(n)
    text = list(text)
    ans = []
    flag = True
    while flag:
        new_text = []  # 단어를 담아둘 리스트 초기화
        for i in range(len(text) - 1):
            if text[i] == text[i + 1]:
                for x in text[i + 2:]:  # 중복 이후부터 담아주기
                    new_text.append(x)
                break
            else:
                new_text.append(text[i])  # 중복 전까지 담아주기
                if i == len(text) - 2:
                    new_text.append(text[i + 1])
        else:
            flag = False  # 중복이 없으면 while 중지

        if flag:  # 중복이 있었으면 새로운 text를 새로운 텍스트로 변환
            text = new_text

    print("#{} {}".format(tc, "".join(map(str, text))))
=======
sys.stdin = open('input.txt')


def push(item):
    stack.append(item)


def pop():
    return stack.pop()


def make_password(s):

    for number in s:
        if stack:
            if stack[-1] == number:
                pop()  # 중복문자 제거
            else:  # 중복이 아닌 문자는 stack에 추가
                push(number)
        else:  # 스택이 비어있다면, stack에 추가
            push(number)

    return stack

for test_case in range(1, 11):
    N, numbers = input().split()  # 문자열의 길이 N
    numbers = list(numbers)

    stack = []

    password = "".join(make_password(numbers))
    print('#{} {}'.format(test_case, password))
>>>>>>> 92ff47ec2ac89df817400374cabd441bfa841964

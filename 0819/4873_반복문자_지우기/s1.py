import sys
<<<<<<< HEAD

sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t + 1):
    text = list(input())
    flag = True
    while flag:
        new_text = []
        for i in range(len(text)-1):
            if text[i] == text[i+1]:
                for x in text[i+2:]:
                    new_text.append(x)
                break
            else:
                new_text.append(text[i])
                if i == len(text)-2:
                    new_text.append(text[i+1])
        else:
            flag = False

        if flag:
            text = new_text

    print("#{} {}".format(tc,len(text)))
=======
sys.stdin = open('sample_input.txt')

def push(item):
    stack.append(item)


def pop():
    return stack.pop()


def delete_duplicated(s):

    for alphabet in s:
        if stack:  # 스택이 비어있지 않고,
            if stack[-1] == alphabet:  # top과 s의 알파벳이 같다면
                pop()  # 중복문자 제거
            else:  # 중복이 아닌 문자는 stack에 추가
                push(alphabet)
        else: # 스택이 비어있다면, stack에 추가
            push(alphabet)

    return len(stack)


T = int(input())
for test_case in range(1, T+1):
    str = input()
    stack = []

    print('#{} {}'.format(test_case, delete_duplicated(str)))
>>>>>>> 92ff47ec2ac89df817400374cabd441bfa841964

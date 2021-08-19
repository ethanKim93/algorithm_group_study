import sys
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

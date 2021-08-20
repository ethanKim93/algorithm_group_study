import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    N, pwd = input().split()
    stack = []   # stack에 문자 하나씩 쌓아가면서 다음 문자랑 같으면 삭제, 없으면 혹은 stack 비어있으면 추가
    for p in pwd:
        if stack:
            if stack[-1] == p:
                stack.pop()
            else:
                stack.append(p)
        else:
            stack.append(p)

    print('#{} {}'.format(tc, ''.join(map(str,stack))))
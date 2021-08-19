import sys
sys.stdin = open("sample_input.txt")

for tc in range(1, int(input())+1):
    strs = input()
    stack = [strs[0]]                  # 단어를 하나씩 쌓을 스택 배열 초기화
    for i in range(1, len(strs)):
        if stack:                      # 스택에 단어가 이미 있는 경우
            if strs[i] == stack[-1]:   # 나오는 단어랑 스택에 맨 위에 쌓인 단어랑 같으면
                stack.pop()            # 스택에 맨 위 단어 제거
            else:
                stack.append(strs[i])  # 같지 않으면 스택에 쌓음
        else:
            stack.append(strs[i])      # 스택에 단어가 없으면 쌓음

    print('#{} {}'.format(tc, len(stack)))

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    text = input()
    stack = []

    for i in text:                          # 입력된 문자를 순회
        if not stack or stack[-1] != i:     # stack이 비어있거나 마지막 항목과 현재 항목이 같지 않으면
            stack.append(i)                 # stack에 추가
        else:                               # stack이 채워져있는데 마지막 항목이 현재 항목과 같으면
            stack.pop()                     # stack에서 마지막 항목 제거
    print('#{} {}'.format(tc, len(stack)))  # 순회 후 남은 stack의 길이 출력
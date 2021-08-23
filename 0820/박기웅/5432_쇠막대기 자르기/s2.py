import sys
sys.stdin = open("sample_input.txt")

'''
stack 사용 풀이
'(' 인 경우 push
'()'인 경우 pop 하고 철봉 개수 추가
나머지 ')' 인 경우 pop하고 철봉 하나 추가
'''
T = int(input())

for tc in range(1, T+1):
    alist = input()
    stack = [alist[0]]
    cnt = 0 
    for i in range(1, len(alist)):
        if alist[i] == '(':
            stack.append(alist[i])
        elif alist[i] == ')' and alist[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1
    print('#{} {}'.format(tc, cnt))
        
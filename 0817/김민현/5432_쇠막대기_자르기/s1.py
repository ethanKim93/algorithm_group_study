import  sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    arr = input()

    stack = []
    cnt = 0
    result = True
    for i in range(0,len(arr)):
        if arr[i] == ')': # 닫는 괄호가 나왔을 경우
             if arr[i-1] == '(': #직전이 여는 괄호 였을 경우(레이저)
                if len(stack) > 0:
                    stack.pop(-1)
                else:
                    pass
                cnt += len(stack)-1

             else:
                 try:
                     stack.pop(-1)
                 except:
                     pass
        else: # 그외 (여는 괄호가 나올때)
            stack.append(arr[i])
            cnt += 1
        p = arr[i]
        c = 1
    print('#{} {}'.format(tc,cnt))


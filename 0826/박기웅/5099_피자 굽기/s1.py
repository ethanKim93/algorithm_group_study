import sys
sys.stdin = open("sample_input.txt")

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    queue, nums = [], []

    # 화덕 크기만큼 초기화
    for i in range(N):
        queue.append(C.pop(0))
        nums.append(i+1)

    while len(queue)!=1:
    
        t = queue.pop(0)//2          # 한 바퀴 돌아서 하나 빼는데 이미 초기화 한 피자는 한바퀴 돌아서 반이 되있음
        n = nums.pop(0)              # 번호도 같이 뺌
        
        if not t and C:              # t가 0 이라서 녹았는데 C에 추가할 피자가 있으면
            queue.append(C.pop(0))   # 남은 C에서 하나꺼내오고
            N += 1
            nums.append(N)           # 다음 번호
        elif not t:                  # t가 0이라 녹았는데 C에 없으면 뺀 상태로 더 이상 뒤에 붙이지 않음
            pass
        else:
            queue.append(t)          # t가 아직 0이 아닌 경우 맨 뒤로
            nums.append(n)           # 꺼낸 번호 다시 뒤에 붙이고

    print('#{} {}'.format(tc, *nums))







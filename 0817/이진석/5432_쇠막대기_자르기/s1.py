for tc in range(1, int(input()) + 1):
    arr = input()
    arr = arr.replace('()', 'L')  # 레이저를 구분하기 위해서 ()를 L로 변경
    answer = 0
    stick = 0
    for i in range(len(arr)):
        if arr[i] == '(':   # i 번째 인덱스가 열리는 괄호라면 (쇠막대기가 시작되는 지점) 쇠막대기 하나 추가
            stick += 1
        elif arr[i] == ')': # i 번째 인덱스가 닫히는 괄호라면 (쇠막대기가 끝나는 지점) 쇠막대기 하나 제거하고
            stick -= 1
            answer += 1     # 최종 막대기 개수에 추가한다.(레이저를 만날때마다 잘리고나면 하나씩 남기 때문)
        elif 0 < i < len(arr) - 1 and arr[i] == 'L':  # 인덱스 유효성 검사(처음과 끝 인덱스에서 레이저가 나오면 아무 일도 일어나지 않음)를 하고,
            answer += stick                           # i 인덱스가 레이저라면, 누적된 쇠막대기의 갯수를 최종 막대기 갯수에 합산(현재 컨트롤중인 쇠막대기가 잘린 상태)

    print('#{} {}'.format(tc, answer))

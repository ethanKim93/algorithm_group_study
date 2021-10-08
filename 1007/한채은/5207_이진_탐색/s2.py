def half(start, end, val, LR="X"):
    if end - start <= 0:
        return 0

    # 가운데껄 반환하게 end에 -1
    m = (start + end - 1) // 2

    # 가운데가 나왔으니까 val(num)
    # 크면 left로 보내기(end대신에 middle)
    if A[m] > val:
        # 왼쪽에서 왼쪽으로 가는 경우를 방지하기 위해 LR이 L이 나오면 0 반환
        return half(start, m, val, "L") if LR != "L" else 0
    # 반대는 가운데 빼고 나머지 보기
    elif A[m] < val:
        # 오른쪽에서 오른쪽으로 가는 경우를 방지하기 위해 LR이 R이 나오면 0 반환
        return half(m + 1, end, val, "R") if LR != "R" else 0
    # 값이 정확할 때만 카운트 하게
    else:
        return 1


for case in range(int(input())):
    N, M = map(int, input().split())

    # A정렬
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    total = 0
    for num in B:
        # start = 0, end = N, val = num
        total += half(0, N, num)

    print("#{} {}".format(case + 1, total))
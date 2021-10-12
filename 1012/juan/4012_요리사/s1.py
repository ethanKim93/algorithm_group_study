def cook(forA, forB, half):
    A = B = 0
    for i in range(half-1):                     # forA, forB 배열의 모든 조합
        for j in range(i, half):
            A += ingredients[forA[i]][forA[j]] + ingredients[forA[j]][forA[i]]
            B += ingredients[forB[i]][forB[j]] + ingredients[forB[j]][forB[i]]
    return abs(A-B)


def combination(half):
    global similar
    for i in range(1, 2**N):
        cnt, used, unused = 0, [], []
        for j in range(N):
            if i & (1 << j):                    # A요리를 위해 사용한 식재료
                cnt += 1
                used.append(j)
            else:                               # A요리에 사용되지 않은 식재료 (= B요리에 사용한 식재료)
                unused.append(j)
        if cnt == half:                         # A요리에 사용한 식재료가 전체 식재료의 절반인 경우만
            gap = cook(used, unused, cnt)       # A요리와 B요리의 맛의 차이를 gap에 저장
            if gap < similar:                   # 전역 similar변수의 값보다 작으면 갱신
                similar = gap


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ingredients = [list(map(int, input().split())) for _ in range(N)]
    similar = 10000 * N

    combination(N//2)
    print('#{} {}'.format(tc, similar))
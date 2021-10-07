# 아래 배열의 부분집합중 합이 10인 부분집합을 구하시오
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 교재에 '{1, 2, 3}의 powerset을 구하는 백트래킹 알고리즘'을 응용해서 풀었다.

def make_candidates(a, k, n, c):
    c[0] = 1
    c[1] = 0


def process_solution(a, k):
    ans = []
    for i in range(1, k+1):
        if a[i] == 1:
            ans.append(i)
    print(ans)


def calc_sum(a, k):
    sumV = 0
    for i in range(1, k+1):
        if a[i] == 1:
            sumV += i
    return sumV


def backtrack(a, k, input):
    c = [0]*2  # 요소가 포함될지 말지 0, 1로 구분
    ncands = 2  # 교재에는 make_candidates에서 2로 바꿔주게 되어있는데 나는 고정시킴
    
    # 부분집합의 합 구하기 -> 10 이상이면 재귀X / 10이면 부분집합 만들기
    if 0 <= k < input:
        sumV = calc_sum(a, k)
        if sumV == 10:
            process_solution(a, k)
        elif sumV > 10:  # 합이 10 넘는 경로는 차단
            return
        else:
            # 인덱스 k번 요소가 0일 때, 1일 때 분기됨
            k += 1
            make_candidates(a, k, input, c)
            for i in range(0, ncands):
                a[k] = c[i]  # 처음엔 1, 끝나고나서 0
                backtrack(a, k, input)  # 재귀호출
    else:  # k가 input값과 같을 때
        sumV = calc_sum(a, k)
        if sumV == 10:
            process_solution(a, k)


powerset = [0] * 11  # powerset을 저장할 배열
backtrack(powerset, 0, len(arr))  # arr의 크기만큼 끝까지 만들어가면서 합이 10보다 큰 길은 자르기로
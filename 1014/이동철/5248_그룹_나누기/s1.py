import sys
sys.stdin = open('sample_input.txt', 'r')


# 싸피 교재 참조
# 유일한 멤버 x를 포함하는 새로운 집합을 생성하는 연산
# 이 문제에서는 굳이 필요 없는 듯
def make_set(x):
    parent[x] = x


# x 를 포함하는 집합을 찾는 연산 
def find_set(x):
    # while x != parent[x]:
    #     x = parent[x]
    # return x
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])
    
    
# x 와 y 를 포함하는 두 집합을 통합하는 연산
def union(x, y):
    parent[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    M_arr = list(map(int, input().split()))
    parent = [i for i in range(N+1)]
    # parent = 출석번호, 0번째는 쓰지 않는다.
    # print(parent)

    for i in range(0, len(M_arr), 2):
        union(M_arr[i], M_arr[i + 1])
    # print(parent)

    result = set()
    for i in range(1, N + 1):
        result.add(find_set(i))
    # print(result)

    print("#{} {}".format(tc, len(result)))
    # print()




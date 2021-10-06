import sys
sys.stdin = open('sample_input.txt')


def permute(nums, r):
    prev_elements = []

    def dfs(elements):
        global minV
        if len(elements) == (len(nums) - r):
            selected_perm = prev_elements[:]
            temp = arr[0][selected_perm[0]] + arr[selected_perm[-1]][0]
            for i in range(0, len(selected_perm) - 1, 1):
                temp += arr[selected_perm[i]][selected_perm[i + 1]]
            if minV > temp:
                minV = temp

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    minV = 987654321
    perm_num = list(range(1, N))

    permute(perm_num, len(perm_num))
    print('#{} {}'.format(tc, minV))

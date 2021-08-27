import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # 피자가 들어오는 순서를 나타내는 pizza_queue와 순서에 대한 인덱스를 나타내는 pizza_idx 선언
    pizza_idx = 0
    pizza_queue = list(map(int, input().split()))

    # 완료된 피자를 순서대로 두는 스택 선언
    pizza_done = []

    # 화덕에서 확인할 인덱스를 나타내는 cook_idx와 화덕 정보를 담은 cook을 선언
    cook_idx = 0
    cook = [[0, 0] for _ in range(N)]

    # 피자의 조리가 모두 완료될 때 까지 반복을 진행한다.
    while len(pizza_done) < M:
        # 원형 큐로 확인하기 위하여 cook_idx에 화덕에 들어갈 수 있는 피자의 수를 나눈 나머지를 새로운 인덱스로 설정
        check_idx = cook_idx % N
        if not cook[check_idx][0] and not cook[check_idx][1]:
            # 화덕이 비어있는 경우, 새로운 피자를 넣는다.
            cook[check_idx][0] = pizza_queue[pizza_idx]
            cook[check_idx][1] = pizza_idx + 1
            pizza_idx += 1
            cook_idx += 1
        else:
            # 화덕이 비어있지 않은 경우, 피자의 치즈를 2로 나눈 몫으로 요리한다.
            cook[check_idx][0] = cook[check_idx][0] // 2

            if not cook[check_idx][0]:
                # 요리가 끝난 경우, 완료된 피자를 스택에 추가한다.
                pizza_done.append(cook[check_idx][1])

                # 모든 피자가 들어왔을 경우, 화덕에 더이상 들어갈 필요가 없으므로,
                # 화덕에 대한 갯수를 조절하고, 확인하는 인덱스를 재 조정한다.
                if pizza_idx >= M:
                    N -= 1
                    cook.pop(check_idx)
                    cook_idx = check_idx
                    continue
                # 들어올 피자가 남았을 경우, 새로운 피자를 넣어준다.
                cook[check_idx][0] = pizza_queue[pizza_idx]
                cook[check_idx][1] = pizza_idx + 1
                pizza_idx += 1
            cook_idx += 1

    print("#{} {}".format(tc, pizza_done[-1]))
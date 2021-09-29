import sys
sys.stdin = open("sample_input.txt")

for tc in range(1, int(input())+1):

    cost = list(map(int, input().split()))
    plan = [0] + list(map(int, input().split()))

    result = [0] * 13


    result[1] = min(cost[0]*plan[1], cost[1])
    result[2] = result[1] + min(cost[0]*plan[2], cost[1])

    for i in range(3, 13):
        result[i] = min(
                        result[i-1] + cost[0] * plan[i],
                        result[i-1] + cost[1],
                        result[i-3] + cost[2]
                        )

    print("#{} {}".format(tc,min(result[12], cost[3])))






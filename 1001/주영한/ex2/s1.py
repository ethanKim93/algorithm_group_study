def check(num_list, visited, cnt, temp_result):
    if cnt == 6:
        front = temp_result[:3]
        rear = temp_result[3:]
        if int(front[2]) - 2 == int(front[1]) - 1 == int(front[0]) and int(rear[0]) == int(rear[1]) == int(rear[2]):
            return True

    for idx in range(len(num_list)):
        if not visited[idx]:
            visited[idx] = 1
            if check(num_list, visited, cnt + 1, temp_result + num_list[idx]):
                return True
            visited[idx] = 0
    return False

def babygin(num_string):
    num_list = num_string
    visited = [0] * len(num_list)
    if check(num_list, visited, 0, ""):
        print('baby-gin!')
    else:
        print('fail')

babygin("124783")
babygin("667756")
babygin("054060")
babygin("101123")
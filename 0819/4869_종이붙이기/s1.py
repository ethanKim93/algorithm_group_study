import sys

sys.stdin = open("input.txt")

t = int(input())
box_list = [1, 3]
for i in range(31):
    box_list.append(box_list[-1] + box_list[-2] * 2)

print(box_list)
for tc in range(1, t + 1):
    size = int(input())
    print("#{} {}".format(tc, box_list[(size // 10) - 1]))

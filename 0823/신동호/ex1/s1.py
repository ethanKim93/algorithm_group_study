formula = input().split()
# 예시는 2 + 3 * 4 / 5 사용
stack = []

for i in formula:
    if i in ['+', '-', '*', '/']:
        stack.append(i)
    else:
        print(i, end = ' ')
for s in range(len(stack)): # for s in stack으로 하면 stack은 감소하는데 s는 인덱스가 하나씩 커져서 전체 순환 못함. 예로 stack이 3개면 2개만 배출되고 끝.
    print(stack.pop(), end = ' ')

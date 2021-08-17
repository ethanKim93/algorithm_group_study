# pythonic

for _ in range(1, 11):
    test_case = int(input())
    pattern = input()
    target = input()
    print('#{} {}'.format(test_case, target.count(pattern)))
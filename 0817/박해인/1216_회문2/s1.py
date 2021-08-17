import sys
sys.stdin = open('input.txt')

for _ in range(10):  # 테스트 케이스 10개 고정
    test_case = int(input())
    arr = [input() for _ in range(100)]

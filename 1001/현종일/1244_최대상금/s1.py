import sys
sys.stdin = open("input.txt")

for tc in range(1, int(input())+1):
    num, cnt = map(int, input().split())
    print(num,cnt)
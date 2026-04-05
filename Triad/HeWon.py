from collections import deque

if __name__ == "__main__":
    no_of_testcases = int(input())

    for _ in range(no_of_testcases):
        n, k = map(int, input().split())

        positions = map(int, input().split())
        power = map(int, input().split())
        table = deque()
        table.append(k)
        i = 0

        # while i < len(power):
        #     if 
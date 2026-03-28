from collections import Counter

if __name__ == "__main__":
    no_of_testcases = int(input())

    for _ in range(no_of_testcases):
        n = int(input())
        sticks = [ int(num) for num in input().strip().split() ]
        occurrence = Counter(sticks)
        # sticks.sort()
        total = 0

        for stick in occurrence:
            total += occurrence[sticks] // 3

        print(total)
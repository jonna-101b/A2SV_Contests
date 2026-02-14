if __name__ == "__main__":
    t = int(input())
    testcases = []

    # read all input first
    for _ in range(t):
        s = input().strip()
        testcases.append(s)

    results = []

    for s in testcases:
        n = len(s)

        # Check infinite sailing
        infinite = False
        for i in range(1, n - 1):
            if s[i] == '*':
                infinite = True
                break

        if infinite:
            results.append(-1)
            continue

        # Finite case
        max_time = 0

        # Moving right
        cur = 0
        for i in range(n):
            if s[i] == '>':
                cur += 1
                max_time = max(max_time, cur)
            else:
                cur = 0

        # Moving left
        cur = 0
        for i in range(n - 1, -1, -1):
            if s[i] == '<':
                cur += 1
                max_time = max(max_time, cur)
            else:
                cur = 0

        results.append(max_time)

    # print all results
    for r in results:
        print(r)

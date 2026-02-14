def solve_case(s):
    n = len(s)
    for i in range(1, n):
        left = s[:i]
        right = s[i:]

        # no leading zeros
        if left[0] == '0' or right[0] == '0':
            continue

        a = int(left)
        b = int(right)

        if b > a:
            return f"{a} {b}"

    return "-1"


if __name__ == "__main__":
    t = int(input())
    testcases = []

    # read all input
    for _ in range(t):
        ab = input().strip()
        testcases.append(ab)

    # process
    results = []
    for ab in testcases:
        results.append(solve_case(ab))

    # output
    for res in results:
        print(res)

def solve_case(s):
    n = len(s)
    INF = 10**9

    # ---------- Strategy 1: Force "2026" ----------
    target = "2026"
    cost_make_2026 = INF

    for i in range(n - 3):
        cost = 0
        for j in range(4):
            if s[i + j] != target[j]:
                cost += 1
        cost_make_2026 = min(cost_make_2026, cost)

    # ---------- Strategy 2: Break all "2025" ----------
    bad_positions = []
    for i in range(n - 3):
        if s[i:i + 4] == "2025":
            bad_positions.append((i, i + 3))

    # Already good
    if not bad_positions:
        cost_break_2025 = 0
    else:
        cost_break_2025 = INF
        # Try all subsets of positions to change (bitmask)
        for mask in range(1, 1 << n):
            changed = set(i for i in range(n) if (mask >> i) & 1)

            ok = True
            for l, r in bad_positions:
                # At least one position in the interval must be changed
                if not any(pos in changed for pos in range(l, r + 1)):
                    ok = False
                    break

            if ok:
                cost_break_2025 = min(cost_break_2025, len(changed))

    return min(cost_make_2026, cost_break_2025)


if __name__ == "__main__":
    t = int(input())
    testcases = []

    # read all input
    for _ in range(t):
        n = int(input())
        s = input().strip()
        testcases.append(s)

    # process
    results = []
    for s in testcases:
        results.append(solve_case(s))

    # output
    for r in results:
        print(r)

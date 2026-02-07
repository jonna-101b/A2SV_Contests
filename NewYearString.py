from collections import defaultdict

PAT25 = "2025"
PAT26 = "2026"
CHARS = ['0', '2', '5', '6']

def advance(pattern, k, ch):
    while k > 0 and pattern[k] != ch:
        k -= 1
    if pattern[k] == ch:
        k += 1
    return k

def solve_case(s):
    n = len(s)
    INF = 10**9

    dp = defaultdict(lambda: INF)
    dp[(0, 0, 0, False, False)] = 0

    for pos in range(n):
        ndp = defaultdict(lambda: INF)
        for (i, a, b, f25, f26), cost in dp.items():
            if i != pos:
                continue
            for ch in CHARS:
                ncost = cost + (ch != s[pos])

                na = advance(PAT25, a, ch)
                nb = advance(PAT26, b, ch)

                nf25 = f25 or (na == 4)
                nf26 = f26 or (nb == 4)

                if na == 4:
                    na = 3
                if nb == 4:
                    nb = 3

                state = (pos + 1, na, nb, nf25, nf26)
                ndp[state] = min(ndp[state], ncost)
        dp = ndp

    ans = INF
    for (pos, a, b, f25, f26), cost in dp.items():
        if pos == n and (f26 or not f25):
            ans = min(ans, cost)

    return ans


if __name__ == "__main__":
    t = int(input())
    testcases = []

    # read all input first
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

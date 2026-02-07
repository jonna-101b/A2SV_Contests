from collections import Counter

def is_subsequence(s, t):
    i = 0
    for ch in t:
        if i < len(s) and s[i] == ch:
            i += 1
    return i == len(s)


def solve_testcase(s, t, p):
    # Condition 1: s must be a subsequence of t
    if not is_subsequence(s, t):
        return "NO"

    cnt_s = Counter(s)
    cnt_t = Counter(t)
    cnt_p = Counter(p)

    # Condition 2: extra chars must be available in p
    for ch in cnt_t:
        needed = cnt_t[ch] - cnt_s.get(ch, 0)
        if needed > cnt_p.get(ch, 0):
            return "NO"

    return "YES"


if __name__ == "__main__":
    q = int(input())
    testcases = []

    # 1) Read all inputs
    for _ in range(q):
        s = input().strip()
        t = input().strip()
        p = input().strip()
        testcases.append((s, t, p))

    # 2) Process & collect outputs
    results = []
    for s, t, p in testcases:
        results.append(solve_testcase(s, t, p))

    # 3) Print all outputs
    for res in results:
        print(res)

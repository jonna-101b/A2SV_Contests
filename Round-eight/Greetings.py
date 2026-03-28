import sys
input = sys.stdin.readline

# Fenwick Tree (BIT)
class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, val):
        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s


t = int(input())
for _ in range(t):
    n = int(input())
    people = [tuple(map(int, input().split())) for _ in range(n)]

    # Sort by starting point a
    people.sort()

    b_vals = [b for _, b in people]

    # Coordinate compression
    sorted_b = sorted(b_vals)
    comp = {v: i+1 for i, v in enumerate(sorted_b)}

    bit = BIT(n)
    ans = 0

    # Count inversions
    for b in reversed(b_vals):
        idx = comp[b]
        ans += bit.query(idx - 1)
        bit.update(idx, 1)

    print(ans)

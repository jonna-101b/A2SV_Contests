t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    a = []
    for _ in range(n):
        a.extend(map(int, input().split()))

    if len(a) == 1:
        print(-1)
        continue

    b = a[1:] + a[:1]

    idx = 0
    for i in range(n):
        row = b[idx:idx+m]
        print(*row)
        idx += m

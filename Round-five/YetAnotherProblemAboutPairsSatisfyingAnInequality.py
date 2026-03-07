import bisect

t = int(input())

for _ in range(t):
    n = int(input())
    a = [0] + list(map(int, input().split()))

    valid = []

    for i in range(1, n+1):
        if a[i] < i:
            valid.append(i)

    ans = 0

    for j in valid:
        pos = bisect.bisect_left(valid, a[j])
        ans += pos

    print(ans)
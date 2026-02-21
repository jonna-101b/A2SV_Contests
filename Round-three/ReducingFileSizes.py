files = []
    total = 0

    for _ in range(n):
        a, b = map(int, input().split())
        total += a
        files.append(a - b)  # saving
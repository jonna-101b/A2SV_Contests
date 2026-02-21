if __name__ == "__main__":
    n, m = [ int(num) for num in input().strip().split() ]
    files = []
    total_size = 0

    for _ in range(n):
        a, b = map(int, input().split())
        total_size += a
        files.append(a - b)

    if total_size <= m:
        print(0)

    else:
        minimum = 0
        files.sort(reverse = True)
        printed = False

        for diff in files:
            minimum += 1
            total_size -= diff

            if total_size <= m:
                print(minimum)
                printed = True
                break
        
        if not printed:
            print(-1)
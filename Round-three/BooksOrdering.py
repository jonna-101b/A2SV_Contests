if __name__ == "__main__":
    n = int(input())
    previous = None

    for i in range(n):
        dimensions = [ int(num) for num in input().strip().split() ]

        if previous is not None and dimensions[0] > previous and dimensions[1] > previous:
            print("NO")
            break

        previous = max(dimensions) if previous is None else (max(dimensions) if max(dimensions) <= previous else min(dimensions))

    else:
        print("YES")
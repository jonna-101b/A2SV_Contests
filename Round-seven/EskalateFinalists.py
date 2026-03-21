if __name__ == "__main__":
    k = int(input().strip())
    r = [ int(num) for num in input().strip().split() ]

    declines = 0
    for rank in r:
        if rank > 25:
            declines = max(declines, rank - 25)

    print(declines)
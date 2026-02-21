if __name__ == "__main__":
    n, k = [ int(num) for num in input().strip().split() ]
    roads = input().strip()
    obstacles = 0
    printed = False

    for road in roads:
        if road == "#":
            obstacles += 1

            if obstacles >= k:
                print("NO")
                printed = True
                break

        else:
            obstacles = 0

    if not printed:
        print("YES")
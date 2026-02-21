if __name__ == "__main__":
    levels = int(input())
    watched = [int(num) for num in input().strip().split()]
    watched.sort()
    printed = False

    for i in range(levels-1):
        if i + 1 != watched[i]:
            print(i + 1)
            printed = True
            break

    if not printed:
        print(levels)
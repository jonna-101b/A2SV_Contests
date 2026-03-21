if __name__ == "__main__":
    n, k = [ int(num) for num in input().strip().split() ]
    layers = sorted(input().strip())
    weight = 0
    prev = None

    for letter in layers:
        if k == 0:
            break

        if prev is not None:
            if ord(letter) - ord(prev) > 1:
                weight += ord(letter) - ord("a") + 1
                k -= 1
        else:
            weight += ord(letter) - ord("a") + 1
            k -= 1

        prev = letter

    if k > 0:
        print(-1)
    else:
        print(weight)
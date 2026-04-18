if __name__ == "__main__":
    n = int(input())
    hws = list(map(int, input().split()))
    hws.sort()
    summation = 0
    i = 0
    j = n - 1

    while i < j:
        summation += (hws[i] + hws[j]) ** 2
        i += 1
        j -= 1

    print(summation)
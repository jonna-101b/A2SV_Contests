if __name__ == "__main__":
    no_of_testcases = int(input())

    for _ in range(no_of_testcases):
        n, k = list(map(int, input().split()))
        costs = list(map(int, input().split()))
        costs.sort(reverse=True)
        eve = 0
        noah = 0
        isEveTurn = True

        for cost in costs:
            if isEveTurn:
                eve += cost
            else:
                noah += cost

            isEveTurn = not isEveTurn

        diff = abs(eve - noah)
        if k > diff:
            print(0)
        else:
            print(diff - k)
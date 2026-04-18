if __name__ == "__main__":
    no_of_testcases = int(input())

    for _ in range(no_of_testcases):
        n, k = list(map(int, input().split()))
        costs = list(map(int, input().split()))
        costs.sort(reverse=True)
        score = 0
        diff = 0
        isEveTurn = True

        for cost in costs:
            if isEveTurn:
                diff = cost
            else:
                needed = diff - cost
                if needed <= k:
                    diff = 0
                    k -= needed
                else:
                    diff -= cost + k
                    k = 0

                score += diff
                diff = 0
                

            isEveTurn = not isEveTurn

        score += diff
        print(score)
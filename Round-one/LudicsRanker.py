if __name__ == "__main__":
    n = int(input())
    ratings = list(map(int, input().split()))

    result = []

    for i in range(n):
        higher = 0
        for j in range(n):
            if ratings[j] > ratings[i]:
                higher += 1
        result.append(higher + 1)

    print(*result)

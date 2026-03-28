if __name__ == "__main__":
    n = int(input())
    weights = [ int(num) for num in input().strip().split() ]
    weights.sort(reverse=True)
    G1 = 0
    G2 = 0

    for weight in weights:
        if G2 <= G1:
            G2 += weight
        else:
            G1 += weight

    print(abs(G2 - G1))
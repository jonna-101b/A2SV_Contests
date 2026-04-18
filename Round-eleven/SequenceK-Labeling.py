from collections import Counter

if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    seq = list(map(int, input().split()))
    occurrence = Counter(seq)
    res = []

    for num in seq:
        if occurrence[num] > k:
            res = []
            break

        res.append(occurrence[num])
        occurrence[num] -= 1

    print("YES" if res else "NO")
    print(*res)
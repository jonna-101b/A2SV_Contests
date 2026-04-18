from collections import Counter

if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    seq = list(map(int, input().split()))
    occurrence = Counter(seq)
    res = []
    max_occurrence = occurrence[seq[0]]

    for num in seq:
        if occurrence[num] > k:
            res = []
            break

        res.append(occurrence[num])
        max_occurrence = max(max_occurrence, occurrence[num])
        occurrence[num] -= 1

    if res:
        i = 0
        for label in range(max_occurrence + 1, k + 1):
            res[i] = label
            i += 1
            
        print("YES")
        print(*res)
    else:
        print("NO")
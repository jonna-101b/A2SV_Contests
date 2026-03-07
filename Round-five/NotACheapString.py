t = int(input())

for _ in range(t):
    w = input().strip()
    p = int(input())

    values = [ord(c) - ord('a') + 1 for c in w]
    total = sum(values)

    if total <= p:
        print(w)
        continue

    chars = [(values[i], i) for i in range(len(w))]
    chars.sort(reverse=True)  # remove largest letters first

    removed = set()

    for value, idx in chars:
        if total <= p:
            break
        total -= value
        removed.add(idx)

    result = []
    for i in range(len(w)):
        if i not in removed:
            result.append(w[i])

    print("".join(result))
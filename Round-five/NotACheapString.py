if __name__ == "main":
    t = int(input())

    for _ in range(t):
        w = input().strip()
        p = int(input())

        price = sum(ord(c) - ord('a') + 1 for c in w)

        chars = [(ord(c) - ord('a') + 1, i) for i, c in enumerate(w)]
        chars.sort(reverse=True)

        removed = [False] * len(w)

        i = 0
        while price > p:
            value, idx = chars[i]
            removed[idx] = True
            price -= value
            i += 1

        result = []
        for i in range(len(w)):
            if not removed[i]:
                result.append(w[i])

        print("".join(result))
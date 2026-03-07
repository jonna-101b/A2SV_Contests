t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    found = False

    for i in range(n):
        last = int(s[i])

        if last % 2 == 1:  # must end with odd digit
            prefix = []
            prefix_sum = 0

            for j in range(i):
                prefix.append(s[j])
                prefix_sum += int(s[j])

                if prefix_sum % 2 == 1:  # prefix sum must be odd
                    res = "".join(prefix) + s[i]

                    if res[0] != '0':  # avoid leading zero
                        print(res)
                        found = True
                        break

            if found:
                break

    if not found:
        print(-1)